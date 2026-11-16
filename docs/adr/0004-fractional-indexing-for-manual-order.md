# 4. Fractional indexing for manual order

- Status: accepted
- Date: 2026-10-31

## Context

Lists and tasks can be reordered by drag and drop. Each move must be cheap, must not rewrite other rows, and must work later when several devices sync changes.

## Decision

Store order as a text key in `position`, generated with fractional indexing: placing an item between two others creates a key that sorts between theirs (for example, between `a0` and `a1`, the key `a0V`). The column uses `COLLATE "C"` so PostgreSQL compares keys byte by byte. The client sends the neighbors of the new position, and only the service computes the key.

## Alternatives considered

- **Integer positions (1, 2, 3...):** easy to understand, but moving one item renumbers every item after it.
- **Decimal positions (1, 1.5, 1.25...):** no renumbering, but floating-point precision runs out after many moves between the same neighbors.

## Consequences

- A move updates exactly one row.
- Keys are not human-readable, and they must never be compared with the database's default collation.
- Clients never need to know the algorithm.
