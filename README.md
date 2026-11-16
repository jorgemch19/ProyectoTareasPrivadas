# Private Tasks

**Your tasks, on your server, depending on no one.**

Private Tasks is a self-hosted task manager and calendar: an open-source alternative to Google Tasks. It runs on your own server with one command, and your data never leaves it.

> **Status:** in early development. Nothing is ready to install yet. Follow the [roadmap](#roadmap) to see progress.

## Why

Your to-do list says a lot about your life. Private Tasks is for people who want to stop depending on external services and companies, and to stay in control of their own tasks.

## Principles

1. **Privacy first.** Your data never leaves your server. No telemetry, no tracking.
2. **Independence.** Works without Google or any other mandatory external service.
3. **Your data is yours.** Export and import everything in open formats.
4. **Simple to install and use.** One command to deploy, and an interface that needs no manual.

## Features (v1)

- Lists with their own icon and color, which you can hide, show and reorder.
- Tasks with description, due date and optional time, subtasks and stars.
- Manual order with drag and drop, or order by date.
- Starred view and search.
- Calendar with month, week and day views.
- Undo for 5 seconds after completing, deleting or moving.
- Import from Google Tasks (via Google Takeout) and export to JSON.
- Light, dark and system themes; Spanish and English.
- Works on mobile and installs as an app (PWA), readable offline.

Planned for later: reminders through [ntfy](https://ntfy.sh), a native Android app with offline sync, and recurring tasks.

## Installation

Installation instructions will be published with the first release. Private Tasks will run with Docker Compose:

```sh
docker compose up -d
```

## Roadmap

| Version | Milestone |
| --- | --- |
| v0.1.0 | Complete API, usable through its interactive documentation |
| v0.2.0 | Web app for daily use in the browser |
| v0.3.0 | Mobile layout and installable PWA |
| v1.0.0 | Official release with documented installation |

## Tech stack

Python, FastAPI and PostgreSQL on the backend; React and TypeScript on the frontend; Docker Compose for deployment. See [ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Documentation

- [Functional specification](docs/SPEC.md): what Private Tasks does.
- [Architecture](docs/ARCHITECTURE.md): how it is built.
- [Roadmap](docs/ROADMAP.md): milestones and their status.
- [Decision records](docs/adr/): why it is built that way.
- [Changelog](CHANGELOG.md).

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first. To report a security issue, follow [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE).
