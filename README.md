# py-app-template

A minimal, modular Python template for building cross-platform desktop applications with minimal setup.

## Overview

This repository provides a small desktop app skeleton with separated `core/` logic, a `gui/` layer, and `resources/` for static assets. It is intended to be easy to extend and package.

Key files and folders
- `main.py` — application entry point
- `config.toml` — runtime configuration
- `main.spec` — PyInstaller spec for building a standalone executable
- `requirements.txt` — runtime dependencies
- `core/` — configuration, enums, managers, utilities
- `gui/` — main window and stage modules
- `resources/` — images, fonts, icons, qss, etc.
- `__app.log` — runtime log file (created at runtime)

## Requirements

- Python 3.8+
- pip
- virtualenv or venv
- PyInstaller for packaging

## Quick start

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
> [!NOTE]
> Configuration is read from `config.toml`. Logs are written to `__app.log`.
## Packaging

To build a standalone executable with PyInstaller (uses `main.spec`):
Adjust `main.spec` or include additional resources from `resources/` as needed.