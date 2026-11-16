# 3. Wall-clock due dates

- Status: accepted
- Date: 2026-10-31

## Context

A task can be due on a day ("Friday") or at a time on a day ("Friday, 18:00"). The usual advice is to store every date in UTC, but an all-day task stored as a UTC instant can appear on the previous or next day when viewed in another timezone.

## Decision

Store due dates as wall-clock values: `due_date` (`date`) and `due_time` (`time`, null for all-day tasks), exactly as the user typed them, and interpret them with the timezone in `settings`. Instants that record when something happened (`created_at`, `completed_at`, `starred_at`, `deleted_at`...) are stored in UTC.

## Alternatives considered

- **One UTC timestamp per task plus an all-day flag:** simpler schema, but every read must convert back to local time, and all-day tasks drift between days when the timezone changes or is misconfigured.

## Consequences

- An all-day task on Friday is always on Friday.
- "Today", overdue tasks and relative dates depend on the configured timezone, which must be set correctly.
- Google Takeout stores dates as UTC instants (`scheduled_time`). The importer converts them to the configured timezone and treats exactly 00:00 as an all-day task, so the timezone must be set before importing.
