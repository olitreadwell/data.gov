# GSA/data.gov context
> refreshed 2026-09-09 | upstream default: main @ 253a03188afe110c00682425deadf9bfd8b7737b

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
- Repo is an infra/meta-ops repo; most open "bugs" track work that lives in sibling app repos (harvester, catalog/ckan) or are assigned to maintainers (marcos-nieto-usds #6287/#6285, Aguiardavidm #6284, rshewitt #6280, jaredb96 #6249). Unassigned open bugs here (#6277 percentage, #6207 org API) reference other apps, not this repo's code.
- No maintainer-engaged, unassigned, code-actionable-in-this-repo issue survives -> self-found gap path (repo-audit).

## Gap ledger (dedupe — READ FIRST, never re-pick)
- `2026-09-03` self-found trivial cleanup (typos, broken markdown link, stale `blob/master` refs, stale `black` comment, `Github`→`GitHub`) — outcome: pr-opened (PR #4) — lesson: pack related trivial fixes into one PR.
- `2026-09-09` self-found code bug `bin/check-and-renew` line 55 uses unset `$wait` instead of re-passing the deploy/space/`--wait` args on recursive re-check — outcome: pr-opened (PR to add) — lesson: verified live; recursion dropped action/space/wait context.

## Mined gaps (discovered, not yet attempted)
- `2026-09-03` `bin/check-and-renew` uses unset `$wait` instead of `$wait_for_app` (line ~142) — status: attempted 2026-09-09 (correct fix = pass `"$action" "$space" --wait` on recursion, not `$wait_for_app` which equals `true` and would never match the `deploy|restart|scale` validator).
