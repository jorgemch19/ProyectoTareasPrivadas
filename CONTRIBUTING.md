# Contributing to Private Tasks

Thanks for your interest. This guide explains how to set up the project and how changes are made.

## Before you start

- Read [SPEC.md](docs/SPEC.md) and [ARCHITECTURE.md](docs/ARCHITECTURE.md). The spec is the source of truth for behavior.
- For anything bigger than a small fix, open an issue first to agree on the approach.
- Keep the [principles](README.md#principles) in mind: no telemetry, no mandatory external services.

## Development setup

Requirements: Docker, [uv](https://docs.astral.sh/uv/) and Node.js (LTS).

```sh
git clone <repository-url>
cd private-tasks
make dev    # starts PostgreSQL, the API and the frontend with hot reload
```

Common commands:

```sh
make test   # backend and frontend tests
make lint   # ruff, mypy, eslint, prettier, tsc
```

Install the pre-commit hooks once with `uvx pre-commit install`.

## Making a change

1. Create a branch from `main` with a type prefix: `feat/`, `fix/`, `docs/` or `chore/`.
2. Keep the change small: one feature or fix per pull request.
3. Add or update tests. Every business rule and API route has tests, and every bug fix starts with a test that reproduces the bug.
4. If the change affects behavior, the API or the data model, update `docs/SPEC.md` or `docs/ARCHITECTURE.md`, and add an entry to `CHANGELOG.md`. Record important decisions as a new ADR in `docs/adr/`.
5. Make sure `make lint` and `make test` pass.
6. Open a pull request and fill in the template.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(tasks): add complete endpoint
fix(import): skip hidden tasks
docs(readme): add installation steps
```

Pull requests are squash-merged, so the pull request title becomes the commit message on `main`.

## Code conventions

- Code, comments, commits and documentation are written in English.
- Backend: type hints everywhere; routes stay thin and business rules live in `services/`; schema changes only through new Alembic migrations.
- Frontend: TypeScript strict mode; every interface text goes through i18n; colors and spacing come from theme tokens.
- No new dependencies without explaining in the pull request why they are needed.

## AI-assisted contributions

AI tools are welcome, but you are responsible for every line you submit. Only open a pull request if you understand and can explain each change.
