# Private Tasks — Functional Specification

This document describes **what** Private Tasks does: its scope, features and business rules. It is the source of truth for behavior. **How** it is built lives in [ARCHITECTURE.md](ARCHITECTURE.md), and **why** key decisions were made lives in [adr/](adr/).

- Status: approved for v1 development
- Applies to: v1.0.0

## 1. Overview

Private Tasks is a self-hosted task manager and calendar, an open-source alternative to Google Tasks. Your tasks live on your own server and depend on no one.

**Audience:** people who want to stop depending on external services and companies, and to stay in control of their own tasks.

**Model:** each person runs their own instance on their own server. An instance has exactly one user.

**License:** MIT.

### Principles

Use these to resolve any doubt about what the product should do.

1. **Privacy first.** Data never leaves the user's server. No telemetry, no tracking.
2. **Independence.** Works without Google or any other mandatory external service.
3. **Your data is yours.** Everything can be exported and imported in open formats.
4. **Simple to install and use.** One command to deploy, and an interface that needs no manual.

## 2. Scope

### v1

- Lists: create, rename, change icon and color, delete, hide or show, reorder.
- Tasks: title, description, due date with optional time, complete, edit, delete, move to another list, star.
- Subtasks, one level deep.
- Manual order (drag and drop) or order by date, chosen per list.
- Starred view and search.
- Calendar with month, week and day views.
- Import from Google Takeout and export to JSON.
- Sign-in for the single user.
- Responsive web app, installable as a PWA, readable offline.
- Light, dark and system themes.
- Interface in Spanish and English.
- Deployment with Docker Compose.

### Later (v2 or after)

- Reminders as push notifications through ntfy.
- Native Android app with offline sync.
- Recurring tasks.
- Dragging tasks in the calendar to change their date.
- Turning a task into a subtask by dragging it.
- Calendar feed (iCal).

### Out of scope

- Multiple users and shared lists.
- Sign-in with Google or any other external provider.
- Connecting to the Google Tasks API (import is file-based only).
- iOS app.
- File attachments.
- Keyboard shortcuts.

## 3. Concepts

| Term | Meaning |
| --- | --- |
| List | A named group of tasks, with an icon, a color, a visibility flag and a sort mode |
| Task | An item in a list. A task with no parent is a *main task* |
| Subtask | A task inside a main task. Subtasks cannot have subtasks |
| Starred task | A task marked with a star. Any task or subtask can be starred |
| Completed task | A task marked as done. It is kept, not deleted |
| Due date | The day a task is due, optionally with a time |
| All-day task | A task with a due date and no time |
| Overdue task | A pending task whose due date is before today |
| Hidden list | A list the user chose not to see in the Tasks columns or the calendar |

"Today" and every date comparison use the timezone set in Settings.

## 4. Features

### 4.1 Sign-in

- A sign-in screen with username and password. There is no sign-up: the user is defined when the instance is installed.
- Sessions last 30 days and renew every time they are used.
- Signing out ends the current session.

### 4.2 Sidebar

- View switch: **Tasks** or **Calendar**.
- Access to the **Starred** view, with its number of tasks.
- Every list, with its icon, color, number of pending main tasks and a button to show or hide it. Hidden lists stay in the sidebar, dimmed.
- A **New list** button and access to **Settings**.
- On mobile the sidebar becomes a slide-out menu.

### 4.3 Lists

- Create a list with a name, an icon (from the Lucide set, with a search box) and a color (from a fixed palette of about 8 colors).
- Rename it and change its icon and color.
- Delete it, after a confirmation that says how many tasks it contains.
- Show or hide it from the sidebar.
- Choose how its tasks are ordered: **manual** (default) or **by date**.
- In the Tasks view, visible lists appear as side-by-side columns of fixed width, scrolling horizontally when they do not fit. Columns are reordered by dragging them left or right.
- On mobile one list is shown at a time, and the user swipes left or right to change list.
- **First run:** there are no lists. The empty state invites the user to create the first list or to import from Google Tasks.

### 4.4 Tasks

- **Add task** button at the top of each column, always visible. A new task appears first in manual order, or in its place in order by date.
- Each task shows a button to complete it, a star to mark it as starred and a three-dot menu with **Delete** and **Move to another list**.
- Clicking a task expands it inside its column to edit the title, description, date and time, and its subtasks. Changes are saved automatically, with no save button.
- Dates are shown in relative form (see 5.4).
- Tasks are reordered by dragging them.
- Completed tasks are grouped at the bottom of each list in a collapsible **Completed (n)** section, collapsed by default. When expanded, they look like normal tasks.
- Completing, deleting or moving a task shows a toast with **Undo** for 5 seconds.

### 4.5 Subtasks

- A subtask works like a task, but lives inside a main task. It has a title, description, date, time and star.
- Subtasks are added from the expanded task with **Add subtask**.
- Subtasks are reordered within their parent.

### 4.6 Starred view

- A special view, not a list. It is opened from the sidebar.
- It gathers the starred tasks and subtasks from every list, including hidden lists. Each task still belongs to its own list.
- Tasks are ordered by when they were starred, most recent first.
- Tasks cannot be created from this view.
- A starred subtask shows which task it belongs to.

### 4.7 Search

- Searches task titles across all lists, including hidden lists and completed tasks.
- Each result shows the list it belongs to.

### 4.8 Calendar

- Three views: **month**, **week** and **day**. Today is highlighted.
- Shows pending tasks with a due date from visible lists. Completed tasks are not shown.
- Each task is a label with the color and icon of its list, and its title (and time, if it has one).
- When a day has more tasks than fit, the ones that fit are shown and the rest are summarized with their list icons and colors and a "+N" indicator.
- Clicking a day in the month or week view opens its day view.
- The **day view** shows only that day's tasks, ordered by time from earliest to latest. Tasks without a time always go last.
- Clicking a task opens it to view or edit it.
- From the day view a task can be created for that day. The user must choose its list first.

### 4.9 Settings

- **Import** from Google Takeout (Tasks.json file). The screen reminds the user to set the correct timezone first.
- **Export** everything to a JSON file.
- **Theme:** system (default), light or dark.
- **Language:** Spanish or English.
- **Timezone:** used for "today", relative dates, overdue tasks and imports.
- **Sessions:** see the devices that are signed in, and sign out one or all of them.

Settings are stored on the server, so they are the same on every device.

### 4.10 Mobile and offline

- The web app adapts to mobile screens and can be installed on Android as a PWA ("Add to home screen").
- Without a connection, it shows the last loaded tasks in read-only mode, with an "offline" notice. Editing requires a connection.

## 5. Business rules

### 5.1 Lists and tasks

| Situation | Behavior |
| --- | --- |
| Delete a list with tasks | The list and all its tasks are deleted, after confirmation |
| Hide a list | It disappears from the Tasks columns and the calendar. It stays in the sidebar, and its starred tasks stay in the Starred view |
| Delete a task with subtasks | Its subtasks are deleted too |
| Move a task to another list | Its subtasks move with it |
| Move a subtask to another list | It becomes a main task in that list |
| Complete a task with subtasks | The task and all its subtasks are completed |
| Uncomplete a completed main task | The task and all its subtasks become pending, including subtasks that were completed earlier on their own |
| Complete a subtask on its own | It goes to the Completed section and shows which task it belongs to (for example, "from: Prepare the exam") |
| Complete the parent afterwards | Its already completed subtasks are grouped inside the completed parent |
| Uncomplete a subtask inside a completed parent | The subtask and its parent become pending; the other subtasks stay completed |
| Complete every subtask | The parent is not completed automatically |
| Create a task from the Starred view | Not allowed |
| Create a task from the calendar | The user must choose its list |
| List counter | Number of pending main tasks, with or without a date. Subtasks are not counted |
| Overdue task | Pending, with a due date before today |

### 5.2 Undo

- Completing, deleting and moving (tasks or lists) can be undone for 5 seconds from the toast.
- Undo restores exactly the state before that action. It is not the opposite action: undoing the completion of a parent only reverts the subtasks completed by that same action, while uncompleting the parent (5.1) reverts all of them.

### 5.3 Ordering

- Each list has a sort mode: manual (default) or by date.
- **By date:** tasks with a date come first, by date and then by time, with all-day tasks after the timed tasks of the same day. Tasks without a date go last.
- **Dragging a task in a list ordered by date** switches the list to manual order. The new manual order starts from the date order being shown, and only the dragged task moves. A toast says "Switched to manual order" with **Undo**.
- **Day view:** by time from earliest to latest; tasks without a time always go last.
- **Starred view:** by when the task was starred, most recent first.

### 5.4 Relative dates

| Due date | Shown as |
| --- | --- |
| Today | Today (with the time if it has one: "Today, 18:00") |
| Tomorrow | Tomorrow |
| Within the next 6 days | Weekday name: "Friday" |
| Later | The date: "Mon, 3 Nov" (with the year if it is not the current year) |
| Yesterday | 1 day ago |
| Several days ago | 3 days ago, 5 days ago... |

## 6. Import and export

### 6.1 Import from Google Takeout

The user exports Google Tasks with Google Takeout and uploads the resulting `Tasks.json`. It contains a list of task lists, each with its tasks. Subtasks appear right after their parent, linked by the `parent` field. Empty fields are omitted, so every field is optional.

| Google Takeout field | Private Tasks field | Notes |
| --- | --- | --- |
| List: `title` | List name | |
| List: `visibility_on_web_fullscreen` | Visible or hidden | `VISIBLE` = visible; any other value = hidden |
| List: `id` | Source reference | Prevents duplicating the list on re-import |
| List: `create_time`, `updated` | Created and updated timestamps | |
| Task: `title` | Title | |
| Task: `notes` | Description | |
| Task: `scheduled_time` (entry with `current: true`) | Due date and, if any, time | Current format: an instant in UTC (see 6.2) |
| Task: `due` | Due date, no time | Older exports; used only if there is no `scheduled_time` |
| Task: `status` (`needsAction` / `completed`) | Pending or completed | |
| Task: `completed` | Completion timestamp | |
| Task: `parent` | Parent task | One level, as in Private Tasks |
| Task: `starred` | Starred | Present only when true |
| Task: `star_time` | Starred timestamp | Used to order the Starred view |
| Task: `created`, `updated` | Created and updated timestamps | |
| Task: `id` | Source reference | Prevents duplicates on re-import |
| Task: `deleted` | Not imported | |
| Task: `hidden` | Not imported | Completed tasks Google hides |
| `kind`, `selfLink`, `task_type` | Ignored | Google internal data |

### 6.2 Import rules

- **Dates:** the `scheduled_time` instant is converted to the timezone set in Settings. If the result is exactly 00:00, the task is imported as an all-day task on that date; otherwise it gets that date and time. Example: `2026-11-03T23:00:00Z` with timezone `Europe/Madrid` becomes an all-day task on 4 November 2026.
- **Order:** tasks keep the order in which they appear in the file as their manual order.
- **Re-import:** lists and tasks already imported (same source reference) are skipped, so importing the same file twice creates nothing new.
- **Imported lists:** get a default icon, and colors assigned in rotation from the palette. The user can change them afterwards.
- **Result:** the import ends with a summary of lists and tasks created and skipped.

### 6.3 Export

- Exports every list and task, including completed ones, to a JSON file. Deleted items are not exported.
- The structure follows Google Takeout, plus Private Tasks fields that Takeout lacks (time, icon, color, visibility, sort mode, position) and a format version number.
- Importing a Private Tasks export restores everything without losing data, so one importer reads both formats.

## 7. Design

- Clean and professional like Google Tasks, with its own personality. Green accent color, neutral typeface.
- Personality comes from the icon and color of each list, a short animation when completing a task, illustrations in empty states and soft, rounded shapes.
- Task states:

| State | Appearance |
| --- | --- |
| Overdue | Semi-transparent red background |
| Starred | Semi-transparent yellow background and star |
| Overdue and starred | Red background, with the star visible |
| Completed | In the collapsible Completed (n) section, normal appearance |

- The approved mockups (Tasks on desktop, Calendar on desktop, Tasks on mobile, in light and dark themes) are the visual reference.

## 8. Non-functional requirements

- **Privacy:** task and list content is never logged. No analytics or calls to external services.
- **Security:** HTTPS, hashed password, revocable sessions, limited sign-in attempts. Details in ARCHITECTURE.md.
- **Accessibility:** keyboard-reachable controls, labels on icon buttons, visible focus and sufficient contrast in both themes.
- **Internationalization:** every interface text is translatable; Spanish and English in v1.
- **Data safety:** documented backup and restore procedure; JSON export as an extra copy.

## 9. Notes for later versions

These features are not in v1, but v1 is designed so they can be added without breaking changes.

- **Reminders (v2):** a reminder at a chosen date and time, separate from the due date, sent through a configurable ntfy server and topic. Cancelled if the task is completed or deleted. Option to hide the task title in the notification. Whether a task allows one or several reminders is still to be decided.
- **Native Android app (v2):** asks for the server URL on first launch, works offline with a local database and syncs with the server.
- **Sync (v2):** the API already accepts client-generated IDs and tracks a change counter, so a sync endpoint can be added later.
