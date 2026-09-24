# GSA/data.gov context
> refreshed 2026-09-25 | upstream default: main @ 4b72003f50db553baafa3985d7aa5c12eb32a2c2

## Identity & policies
- upstream: GSA/data.gov, default branch `main`, primary language: Python/Shell/Markdown (small infra/ops/docs repo: bin/ shell scripts + GitHub Actions templates + docs)
- English-first: yes (all docs in English)
- CLA/DCO: none (no CLA bot, no contributor agreement in CONTRIBUTING.md)
- AI-assisted PR policy: unstated (no mention in CONTRIBUTING.md, PR template, README, docs, or GSA/.github org defaults — org `.github` CONTRIBUTING/PULL_REQUEST_TEMPLATE/profile all 404)
- signed commits required: no (no branch protection on `main`)
- PR template: `.github/pull_request_template.md` (fill verbatim)
- external tracker: github (issues + org Projects board)

## Conventions (verified from merged PRs)
- branch naming: mixed — `fix-*`, `update-*`, `6260-*`, `SueValente-*`, `dependabot/*`, feature branches; no dominant pattern. Fall back to `type/desc`.
- commit style: plain imperative ("Update GitHub onboarding tasks", "correct the link"); occasional `fix:`/`6260:` prefixes. Use plain imperative.
- CI: GitHub Actions workflows (snyk, ckan-test, deploy templates). No lint/test gate on bin/ shell scripts or docs; no shellcheck in CI.
- outside PRs merge: yes, small doc/link/typo PRs from outsiders merge (fix-link, update-badge-link, remove badge link).

## Maintainer picture
- active maintainers: GSA Data.gov team (marcos-nieto-usds, jpyuda, rshewitt, jaredb96, Aguiardavidm, SueValente, jbrown-xentity, FuhuXia).
- areas actively worked: GitHub Actions templates, deploy/restart/scale ops, onboarding checklists, DCAT-US3 harvest sources, harvester/snyk findings.

## Issue-area health
- Repo is an infra/meta-ops repo; most open "bugs" track work that lives in sibling app repos (harvester, catalog/ckan) or are assigned to maintainers. Issue #6343 (per-org metrics reports empty for orgs with & in name) IS in this repo's metrics code but already has an OPEN upstream fix PR #6344 (soroush5, use raw org name) — claimed, do NOT duplicate. Remaining unassigned bugs reference other apps.
- metrics/ module is the one real, testable app in this repo (GA + CKAN -> S3 CSV reports); established test pattern (metrics/tests/test_csv_encoding.py) added 2026-09 with the CSV-encoding fix.
- No maintainer-engaged, unassigned, code-actionable-in-this-repo issue survives -> self-found gap path (repo-audit).

## Gap ledger (dedupe — READ FIRST, never re-pick)
- `2026-09-03` self-found trivial cleanup (typos, broken markdown link, stale `blob/master` refs, stale `black` comment, `Github`→`GitHub`) — outcome: pr-opened (PR #4) — lesson: pack related trivial fixes into one PR.
- `2026-09-09` self-found code bug `bin/check-and-renew` line 55 uses unset `$wait` instead of re-passing the deploy/space/`--wait` args on recursive re-check — outcome: pr-opened (PR #7) — lesson: verified live; recursion dropped action/space/wait context.
- `2026-09-25` self-found test-coverage gap: metrics/datagov_metrics/catalog.py `get_data()` + `write_data_to_csv()` have ZERO test coverage; the only metrics tests (test_csv_encoding.py) cover ga.py/s3_util.py. Outcome: pr-opened (PR #8).

## Mined gaps (discovered, not yet attempted)
- `2026-09-03` `bin/check-and-renew` uses unset `$wait` instead of `$wait_for_app` (line ~142) — status: attempted 2026-09-09 (correct fix = pass `"$action" "$space" --wait` on recursion, not `$wait_for_app` which equals `true` and would never match the `deploy|restart|scale` validator).
- `2026-09-25` tests-ci `metrics/datagov_metrics/catalog.py` (get_data two-query fetch+reshape, write_data_to_csv header/rows, main error path) unpiloted — status: attempted (PR #8, add metrics/tests/test_catalog.py following test_csv_encoding.py stub pattern; pure unit tests, no deps).
