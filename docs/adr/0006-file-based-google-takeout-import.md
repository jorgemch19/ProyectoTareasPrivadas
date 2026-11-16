# 6. File-based import from Google Takeout

- Status: accepted
- Date: 2026-10-31

## Context

Most users will come from Google Tasks, so importing their data is essential. Google offers two ways to get it: the Google Tasks API, and a Google Takeout export file (`Tasks.json`).

## Decision

Import only from the Takeout file, uploaded in Settings. The importer is lenient: every field is optional, unknown fields are ignored, it supports both the current date format (`scheduled_time`) and the older one (`due`), and it is idempotent through `source_id`.

## Alternatives considered

- **Google Tasks API with OAuth:** one click for the user, but each self-hosted instance would need its own Google Cloud project and OAuth credentials, which is heavy friction and contradicts the independence principle.

## Consequences

- Migration needs a few manual steps in Google Takeout, which the documentation explains.
- No Google dependency at runtime.
- Takeout's format is not formally documented and may change; sample files in the tests protect against regressions.
