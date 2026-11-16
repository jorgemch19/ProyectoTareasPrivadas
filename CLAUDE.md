# CLAUDE.md

Guidance for AI coding agents working on **Private Tasks**. Read this file, `docs/SPEC.md`, `docs/ARCHITECTURE.md` and `docs/ROADMAP.md` before making any change.

## Project

Private Tasks is a self-hosted, single-user task manager and calendar: an open-source alternative to Google Tasks. MIT licensed.

Principles (use them to resolve doubts):

1. **Privacy first**: user data never leaves the user's server. No telemetry, no tracking.
2. **Independence**: no mandatory external services (no Google, no third-party APIs).
3. **Your data is yours**: everything can be exported and imported in open formats.
4. **Simple to install and use**: one command to deploy, a UI that needs no manual.

## Roles

- **The maintainer is the product director.** They decide scope, priorities and design, approve plans and results, and manage GitHub (pushing, pull requests, merges).
- **You are the developer.** You write the code, tests and documentation, following SPEC.md, ARCHITECTURE.md and this file. You decide technical details already covered by those documents; record any important new technical decision as an ADR and mention it in your report.
- **Language:** talk to the maintainer in Spanish, in plain words aimed at a director, not a developer. Code, comments, commits and documentation stay in English.
- Prefer simple, readable code over clever code.

## Stack

- Backend: Python (latest stable), FastAPI, SQLAlchemy 2 (sync), Alembic, Pydantic, uv.
- Database: PostgreSQL.
- Frontend: React, TypeScript, Vite, TanStack Query, Tailwind, shadcn/ui, Lucide icons, dnd-kit, FullCalendar, react-i18next, vite-plugin-pwa.
- Deployment: one Docker image (API + built frontend) + PostgreSQL, Docker Compose, optional Caddy.

## Repository map

```
backend/app/api/        HTTP routes only: parse input, call a service, return output
backend/app/services/   Business rules (the only place where rules live)
backend/app/models/     SQLAlchemy tables
backend/app/schemas/    Pydantic request/response models
backend/app/core/       Configuration, security, sessions
backend/migrations/     Alembic migrations
backend/tests/          pytest
frontend/src/           React app
docs/                   SPEC.md, ARCHITECTURE.md, ROADMAP.md, adr/
deploy/                 compose.yml, Caddyfile, .env.example
```

## Commands

```
make dev     # start PostgreSQL (compose.dev.yml), API and frontend in dev mode
make test    # backend and frontend tests
make lint    # ruff, mypy, eslint, prettier, tsc
```

Run `make lint` and `make test` before declaring any task done. If a command fails, fix the cause; never skip, disable or weaken a check to make it pass.

## Workflow rules

1. **Plan before coding.** Work milestone by milestone, following `docs/ROADMAP.md`. Before starting one, present a short plan in Spanish: what will be built, how it will be split into pull requests, and anything the director must decide. Wait for approval.
2. **Small steps.** One feature or fix per pull request. Do not change code outside the task's scope; mention unrelated problems instead of fixing them.
3. **Tests first or alongside.** Every business rule and every API route has tests. Every bug fix starts with a test that reproduces the bug.
4. **Ask before adding a dependency** that the documents do not already list. Explain why it is needed and what the alternative is.
5. **Git.** Create a branch from an up-to-date `main` (`feat/`, `fix/`, `docs/`, `chore/`) and commit locally with Conventional Commits messages, e.g. `feat(tasks): add complete endpoint`. **Never push, never merge, and never touch `main`**: the director pushes, opens the pull request and merges.
6. **Keep docs in sync.** If a change affects behavior, the API or the data model, update `docs/SPEC.md` or `docs/ARCHITECTURE.md` and `CHANGELOG.md` (Keep a Changelog) in the same branch. Record important decisions as a new ADR in `docs/adr/`.
7. **When unsure, ask.** Do not guess product requirements; the spec is the source of truth. Product changes are the director's decision.
8. **Report when a branch is ready.** In Spanish: what was done, how the director can try it (exact steps), decisions taken, and anything pending. Then give the pull request title and description in English, filled in following `.github/pull_request_template.md`, ready to paste.

## Backend conventions

- Type hints everywhere; code must pass `mypy` and `ruff`.
- Routes are thin. All rules (completing with subtasks, undo, moving, ordering, import) live in `services/` and are unit tested there.
- API under `/api/v1`, JSON in `snake_case`. Errors always use the same shape: an error code and a message.
- Actions with rules have their own routes (`POST /tasks/{id}/complete`), not generic field updates.
- Create routes accept an optional client-generated UUID and are idempotent.
- **Soft delete:** never hard-delete lists or tasks. Set `deleted_at`, and always filter out deleted rows in queries.
- **Undo:** every row affected by one action gets exactly the same timestamp (`completed_at` or `deleted_at`); undo reverts only rows with that timestamp.
- **Ordering:** `position` uses fractional indexing, computed only in the service from the neighbors the client sends.
- **Dates:** `due_date` and `due_time` are wall-clock values interpreted with the timezone in `settings`. Control timestamps (`created_at`, `updated_at`, `completed_at`, `starred_at`, `deleted_at`) are UTC.
- Every change to `lists` or `tasks` updates `updated_at` and takes a new `sync_seq` from the PostgreSQL sequence.
- Subtasks have exactly one level: a subtask can never have subtasks. Validate this in the service.
- Schema changes only through new Alembic migrations. Never edit a migration that is already merged.

## Frontend conventions

- TypeScript strict mode; no `any` without a comment explaining why.
- Server data only through TanStack Query; use optimistic updates for complete, delete and move, with the 5-second undo toast.
- No hard-coded UI text: every string goes through react-i18next (Spanish and English).
- Colors, spacing and radii come from the theme tokens (CSS variables) so light, dark and system themes work everywhere.
- Accessibility: real `<button>`, `<a>`, `<input>` and `<label>` elements, `aria-label` on icon-only buttons, visible focus, sufficient contrast.
- Follow the approved mockups (Design canvas "Private Tasks: bocetos").

## Security and privacy (never break these)

- Never log task or list content. Log errors and requests only.
- Never commit secrets; configuration comes from `.env` (document new variables in `.env.example`).
- Credentials: `PT_USERNAME` and `PT_PASSWORD_HASH` (Argon2) in `.env`. Sessions live in the `sessions` table, sent as an HttpOnly, Secure, SameSite cookie (web) or a Bearer token (mobile), expiring after 30 days of inactivity.
- Validate every input with Pydantic and explicit limits.
- PostgreSQL is never exposed outside the internal Docker network.
- Never add analytics, tracking or calls to external services.
