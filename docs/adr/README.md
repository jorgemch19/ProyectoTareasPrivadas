# Architecture Decision Records

Each file records one important decision: its context, the option chosen, the alternatives considered and the consequences.

Rules:

- One decision per file, numbered in order: `NNNN-short-title.md`.
- Accepted records are never edited. If a decision changes, write a new record and mark the old one as `superseded by NNNN`.

| # | Decision | Status |
| --- | --- | --- |
| [0001](0001-postgresql-as-database.md) | PostgreSQL as the database | accepted |
| [0002](0002-database-sessions-instead-of-jwt.md) | Database sessions instead of JWT | accepted |
| [0003](0003-wall-clock-due-dates.md) | Wall-clock due dates | accepted |
| [0004](0004-fractional-indexing-for-manual-order.md) | Fractional indexing for manual order | accepted |
| [0005](0005-soft-delete-and-shared-action-timestamps.md) | Soft delete and shared action timestamps | accepted |
| [0006](0006-file-based-google-takeout-import.md) | File-based import from Google Takeout | accepted |
| [0007](0007-single-user-per-instance.md) | One user per instance | accepted |

Template:

```markdown
# N. Title

- Status: proposed | accepted | superseded by NNNN
- Date: YYYY-MM-DD

## Context
## Decision
## Alternatives considered
## Consequences
```
