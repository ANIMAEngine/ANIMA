# Development Rules

These rules must be respected throughout the lifetime of the project.

---

## General Rules

One class = One responsibility.

One file = One purpose.

Keep code readable.

Document before coding.

Never hardcode values that belong in data files.

---

## Architecture Rules

UI never contains simulation logic.

Simulation never depends on UI.

Modules communicate only through public interfaces.

Avoid circular imports.

---

## Git Rules

One feature per commit.

Meaningful commit messages.

Never push broken code.

---

## Documentation Rules

Every new system requires documentation before implementation.

Architecture changes must be documented.

---

## Code Style

Use type hints.

Use dataclasses when appropriate.

Write docstrings.

Keep functions small.

Avoid global variables.