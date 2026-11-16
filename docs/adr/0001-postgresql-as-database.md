# 1. PostgreSQL as the database

- Status: accepted
- Date: 2026-10-31

## Context

Private Tasks needs a relational database for lists, tasks, settings and sessions. It is self-hosted by people with different levels of experience, and it is also a learning project for its maintainer.

## Decision

Use PostgreSQL, accessed through SQLAlchemy 2 with Alembic migrations, running as a second container in Docker Compose.

## Alternatives considered

- **SQLite:** a single file, no extra container, trivial backups, and more than enough performance for one user. Rejected because the project aims to teach the tools used in professional work, and because PostgreSQL features (sequences for the change counter, `"C"` collation for ordering keys, robust concurrent access for a future sync endpoint) fit the design directly.

## Consequences

- An instance runs two containers instead of one; Docker Compose hides most of that cost.
- Backups need `pg_dump` instead of copying a file, so the procedure must be documented.
- Tests run against a real PostgreSQL in CI, never against SQLite, so they behave like production.
