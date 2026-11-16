# Private Tasks — Roadmap

v1 is built bottom-up in 12 milestones: foundation, complete backend, web app, deployment. Each milestone is split into one or more small pull requests. A milestone is done only when its "done when" criterion is met.

Mark a milestone as done here, in the same pull request that completes it.

| # | Milestone | Includes | Done when | Status |
| --- | --- | --- | --- | --- |
| 0 | Repository skeleton | Folder structure with minimal backend and frontend apps, Makefile, pre-commit, `compose.dev.yml`, CI, Dependabot | CI passes and `make dev` starts PostgreSQL | pending |
| 1 | Backend foundation | FastAPI, settings from `.env`, database connection, Alembic, `/health`, error format, tests against real PostgreSQL | `/health` answers in tests and migrations run at startup | pending |
| 2 | Authentication | `sessions` table, `hash-password` command, login and logout, cookie and Bearer token, session list and revocation, sign-in rate limit | Tests cover valid and invalid login, expiry, revocation and rate limit | pending |
| 3 | Lists | Model, routes, reorder, visibility, sort mode, counters, delete and undo | Every list rule in SPEC.md has a test | pending |
| 4 | Tasks | Four parts: create and edit with subtasks and stars; complete, uncomplete and undo; move and reorder; queries (starred, calendar range, search) | Every task rule in SPEC.md has a test | pending |
| 5 | Settings, import, export | Settings routes, Google Takeout import, JSON export | Importing the samples creates what is expected, re-importing creates nothing, and export then import round-trips | pending |
| 6 | Frontend foundation | React app, light/dark/system themes, Spanish and English, sign-in, sidebar, API client | Sign in and see the empty sidebar in both themes and languages | pending |
| 7 | Tasks view | Four parts: list columns; tasks with inline editing, subtasks, completed section and undo; drag and drop; starred view and search | Everything in the Tasks mockups works against the real API | pending |
| 8 | Calendar | Month, week and day views, labels, crowded days, create from a day | Works like the interactive calendar mockup | pending |
| 9 | Settings screen | Settings UI, import and export from the interface, sessions | A user migrates from Google Tasks without using a terminal | pending |
| 10 | Mobile and PWA | Responsive layout, swipe between lists, installable PWA, offline read-only | Installs on Android and shows tasks offline | pending |
| 11 | Deployment and v1.0 | Dockerfile, `compose.yml` with optional Caddy, Ubuntu installation guide, backup and update guide, image publishing, end-to-end tests, README with screenshots | Someone new to the project installs it by following only the README | pending |

## Releases

- **v0.1.0** after milestone 5: complete API, usable through `/api/docs`.
- **v0.2.0** after milestone 7: daily use in the browser.
- **v0.3.0** after milestone 10: also on mobile.
- **v1.0.0** after milestone 11: official release.

Between milestones 5 and 6, deploy the API to the director's Ubuntu VPS, to find deployment problems early.
