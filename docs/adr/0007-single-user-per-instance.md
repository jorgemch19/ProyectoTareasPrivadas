# 7. One user per instance

- Status: accepted
- Date: 2026-10-31

## Context

Private Tasks is self-hosted: each person runs their own instance. Supporting several accounts means registration, password recovery, permissions and filtering every query by user, which is a classic source of data-leak bugs.

## Decision

Each instance has exactly one user, defined by `PT_USERNAME` and `PT_PASSWORD_HASH` in the environment. There is no users table and no public sign-up.

## Alternatives considered

- **A users table with a single row:** ready for multiple users later, but it adds code and concepts that v1 does not use.

## Consequences

- The data model and every query are simpler.
- Changing the password means generating a new hash and restarting the container.
- Multi-user support and shared lists are out of scope. Adding them later would need a migration that introduces a users table and ownership columns, recorded in a new ADR.
