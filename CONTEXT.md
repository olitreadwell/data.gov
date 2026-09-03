# GSA/data.gov context
> refreshed 2026-09-03 | upstream default: main @ cb5d8bb7f31a8da0813a272a14c05ee390f094ee

## Identity & policies
- upstream: GSA/data.gov, default branch `main`, primary language: Python/Shell/Markdown (small ops/docs repo)
- English-first: yes (all docs in English)
- CLA/DCO: none (no CLA bot, no contributor agreement in CONTRIBUTING)
- AI-assisted PR policy: unstated (no mention in CONTRIBUTING or templates)
- signed commits required: no (no branch protection on `main`)
- PR template: `.github/pull_request_template.md` (fill verbatim)
- external tracker: github (issues + org Projects board)

## Conventions (verified from merged PRs)
- branch naming: mixed — `fix-*`, `update-*`, `6260-*`, `SueValente-*`, `dependabot/*`; no dominant pattern. Fall back to `type/desc`.
- commit style: plain imperative ("Update GitHub onboarding tasks", "correct the link"); occasional `fix:`/`6260:` prefixes. Use plain imperative.
- CI: GitHub Actions workflows (snyk, ckan-test, deploy templates). No lint/test gate on this repo's own docs.
- outside PRs merge: yes, small doc/link/typo PRs from outsiders merge (e.g. `fix-link`, `update-badge-link`, `correct the link`).

## Maintainer picture
- active maintainers: GSA Data.gov team; responsive to small doc/link PRs (recent merged `fix-link`, `update-badge-link`).
- areas actively worked: GitHub Actions templates, onboarding/offboarding checklists, harvest source management.

## Issue-area health
- docs/issue-template area is low-contention; small cleanup PRs welcome.
- no contested/redesign signals in docs area.

## Gap ledger (dedupe — READ FIRST, never re-pick)
- `2026-09-03` self-found trivial cleanup (typos, broken markdown link, stale `blob/master` refs, stale `black` comment, `Github`→`GitHub`) — outcome: pr-opened — lesson: pack related trivial fixes into one PR.

## Mined gaps (discovered, not yet attempted)
- `2026-09-03` `bin/check-and-renew` uses unset `$wait` instead of `$wait_for_app` (line ~142) — status: proposed (code bug, out of trivial-doc scope; revisit for a code-fix PR).
