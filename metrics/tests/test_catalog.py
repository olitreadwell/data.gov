"""Unit tests for the catalog-metrics report module (datagov_metrics/catalog.py).

catalog.py talks to CKAN-style APIs and S3; this test stubs those I/O layers so
the pure reshaping logic runs anywhere without credentials or network.
"""

import sys
import types
import unittest
from unittest.mock import MagicMock, patch


def _load_catalog():
    # Stub the heavy third-party deps (same approach as test_csv_encoding.py)
    # so importing catalog/ga/s3_util works without GA creds or AWS config.
    google = types.ModuleType("google")
    oauth2 = types.ModuleType("google.oauth2")
    service_account = types.ModuleType("google.oauth2.service_account")
    service_account.Credentials = MagicMock()
    discovery = types.ModuleType("googleapiclient.discovery")
    discovery.build = MagicMock(return_value=MagicMock())
    boto3 = types.ModuleType("boto3")
    boto3.client = MagicMock(return_value=MagicMock())
    dotenv = types.ModuleType("dotenv")
    dotenv.load_dotenv = MagicMock()
    requests = types.ModuleType("requests")
    requests.RequestException = type("RequestException", (Exception,), {})
    requests.get = MagicMock()  # so patch.object can target catalogs call site

    sys.modules["google"] = google
    sys.modules["google.oauth2"] = oauth2
    sys.modules["google.oauth2.service_account"] = service_account
    sys.modules["googleapiclient"] = types.ModuleType("googleapiclient")
    sys.modules["googleapiclient.discovery"] = discovery
    sys.modules["boto3"] = boto3
    sys.modules["dotenv"] = dotenv
    sys.modules["requests"] = requests

    sys.path.insert(0, ".")
    from datagov_metrics import catalog

    return catalog, requests


catalog, requests_mod = _load_catalog()

ORG = {"slug": "epa", "source_count": 5, "dataset_count": 12, "name": "EPA"}


def _ok(json_data):
    r = MagicMock()
    r.json.return_value = json_data
    r.raise_for_status.return_value = None
    return r


class TestGetData(unittest.TestCase):
    def test_returns_both_reports_with_expected_keys(self):
        catalog_resp = {"organizations": [dict(ORG, dataset_count=99)]}
        with patch.object(requests_mod, "get") as get:
            get.side_effect = [_ok([ORG]), _ok(catalog_resp)]

            output, errors = catalog.get_data()

        self.assertEqual(errors, [])
        self.assertIn("harvest_sources", output)
        self.assertIn("datasets_per_org", output)
        # harvest_sources uses source_count
        self.assertEqual(output["harvest_sources"], [["epa", 5]])
        # datasets_per_org uses dataset_count
        self.assertEqual(output["datasets_per_org"], [["epa", 99]])

    def test_surfaces_failure_among_reports(self):
        with patch.object(requests_mod, "get") as get:
            r = MagicMock()
            r.raise_for_status.side_effect = requests_mod.RequestException("boom")
            get.side_effect = [r, _ok({"organizations": [ORG]})]

            output, errors = catalog.get_data()

        # the failing query is reported, the healthy one still comes through
        self.assertEqual(len(errors), 1)
        self.assertIn("harvest_sources", errors[0])
        self.assertEqual(output["datasets_per_org"], [["epa", 12]])


class TestWriteDataToCsv(unittest.TestCase):
    def test_writes_header_then_rows(self):
        lines = catalog.write_data_to_csv([["epa", 5], ["hhs", 2]]).strip().splitlines()
        self.assertEqual(lines[0], "organization,count")
        self.assertIn("epa,5", lines)
        self.assertIn("hhs,2", lines)

    def test_empty_payload_still_writes_header(self):
        self.assertEqual(catalog.write_data_to_csv([]).strip(), "organization,count")


if __name__ == "__main__":
    unittest.main()
