# 5. Soft delete and shared action timestamps

- Status: accepted
- Date: 2026-10-31

## Context

Completing, deleting and moving can be undone for 5 seconds. Some actions affect many rows: deleting a list deletes its tasks, and completing a task completes its subtasks. Undo must restore exactly the state before the action, without touching rows changed earlier. Later, synced devices must also learn about deletions.

## Decision

- Never hard-delete lists or tasks in v1: set `deleted_at` instead, and filter deleted rows in every query.
- Give every row changed by one action exactly the same `completed_at` or `deleted_at` value.
- Undo uses a short-lived signed token that identifies the action and its timestamp; it reverts only the rows carrying that timestamp, and refuses with `undo_conflict` if those rows changed since.

## Alternatives considered

- **Hard delete plus a copy for undo:** loses the information needed for sync and makes undo of large deletions expensive.
- **An undo log table:** flexible, but adds a table and cleanup for something a timestamp already identifies.

## Consequences

- Undo of "complete a parent" restores only the subtasks completed in that action; subtasks completed earlier stay completed.
- Deleted rows accumulate. Purging rows deleted more than 30 days ago arrives with sync in v2.
- Forgetting the `deleted_at IS NULL` filter is a real risk; tests must cover it for every query.
