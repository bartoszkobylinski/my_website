# my_website — Roadmap

Last reviewed: 2026-10-19 · Reviewed against: d5c15fb
Product: standalone · Product roadmap: this file

Personal website of Bartosz Kobylinski: a one-route Flask app (`app/routes.py`) that renders a
single static page (`app/templates/main.html`) with a short bio, the public project lovspor /
lovverk and contact links. The last change is the minimalist 2026 redesign (2026-05-08); the
repository records no further plans.

## Now
- Remove the 2020 CV PDF that was still served at `/static/cv/` with no page linking it (owner, 2026-10-19) — this PR deletes `app/static/cv/bartosz_kobylinski_cv.pdf`; the live site drops it on its next deploy

## Next
- (none recorded)

## Later
- (none recorded)

## Done
2026 redesign
- Cache-bust `main_style.css` with a versioned query string after a stale CDN copy broke the page — `d5c15fb`
- Minimalist single-page redesign: one route, lovspor / lovverk project section, removed the
  about-me, projects, milamber and thanks pages, the contact form and its mail/form dependencies;
  `requirements.txt` reduced to `Flask==2.3.2` — `83c969f`

2023 rework (superseded by the 2026 redesign)
- Server errors shown as flash messages — `e7a8cd8`
- Milamber interaction page and styling updates — `bceb42b`
- Email sending removed from routes — `95687d3`
- App structure refactored for Gunicorn — `22d74b9`
- Logging, refactor and new design/content — `d3fb229`; requirements and favicons — `339b197`

2019–2022 first version (superseded)
- Google Analytics added — `7b4d420`
- Contact form with mail sending, validation and an anti-spam question — `1fd4bc7`, `e0ae84e`, `00ae6a8`
- CV page with an embedded/downloadable PDF — `613c132` … `d569ec5`
- Grid-based layout, mobile-first CSS, hamburger menu — `a1afdfd`, `11ecbfe`, `29d69ae`
- Initial site — `754a09b`

## Unverified
- Dependabot PR #2 (urllib3 2.0.4 → 2.0.7) and PR #3 (werkzeug 2.3.6 → 3.0.1), open since
  October 2023 — both edit pins that `83c969f` removed from `requirements.txt`; whether they will
  be closed or rebased is not recorded.
- Deployment (host, Gunicorn entry point, CDN) — commit messages mention Gunicorn (`22d74b9`) and a
  CDN cache (`d5c15fb`), but the repository holds no deploy configuration; the live setup cannot be
  checked from the repo.

## Sources
- Repository tree at `d5c15fb` (`app/routes.py`, `app/templates/main.html`, `app/static/`,
  `requirements.txt`, `.gitignore`); no README, CLAUDE.md, AGENTS.md or docs exist
- `git log` of `master` (61 commits) and remote branches (`feat/redesign-2026`, `fix/cache-bust-css`,
  `new_design` — all contained in `master`; two Dependabot branches)
- `gh issue list -R bartoszkobylinski/my_website --state all -L 200` (no issues)
- `gh pr list -R bartoszkobylinski/my_website --state all -L 200` (PRs #1 closed, #2 and #3 open)
