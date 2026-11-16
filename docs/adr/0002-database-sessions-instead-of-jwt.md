# 2. Database sessions instead of JWT

- Status: accepted
- Date: 2026-10-31

## Context

The web app and, later, the Android app must stay signed in for weeks. If a device is lost, the user must be able to sign it out remotely.

## Decision

Store sessions in a `sessions` table. Login creates a random 256-bit token; only its SHA-256 hash is stored. The web sends it in an `HttpOnly`, `Secure`, `SameSite=Strict` cookie, and the mobile app in an `Authorization: Bearer` header. Sessions expire 30 days after their last use and can be revoked one by one or all at once.

## Alternatives considered

- **JWT:** stateless and widely used, but a JWT stays valid until it expires and cannot be revoked without adding a denylist, which brings back the database lookup it was meant to avoid. It is also harder to reason about for a learning project.

## Consequences

- Every authenticated request reads the `sessions` table. For one user this cost is negligible.
- The user can see signed-in devices and sign them out.
- A database leak does not expose usable tokens, because only hashes are stored.
