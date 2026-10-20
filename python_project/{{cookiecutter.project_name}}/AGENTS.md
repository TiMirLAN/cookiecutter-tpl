# AGENTS.md

Guidance for AI coding agents working on {{ cookiecutter.project_name }}.

## Instruction files

1. Read this file first.
2. Then read `LOCAL_AGENTS.md` in this directory, if it exists. It describes the local development environment, is gitignored, and **takes priority over `AGENTS.md`** when they conflict.

Never commit `LOCAL_AGENTS.md`.

## Overview

Typed Python {{ cookiecutter.python_version }}+ package using a `src/` layout. Tooling: uv, hatchling, pydantic-settings, ruff, pyright, pytest + pytest-cov, pre-commit.

- `src/{{ cookiecutter.project_slug }}/` — package source (`settings.py` holds the `Settings` class, read from `.env`)
- `tests/` — pytest suite
- `template.env` — documented environment variables; copy to `.env` (gitignored)

## Commands

```bash
make sync        # uv sync
make lint        # ruff check + format check
make fmt         # ruff fix + format
make typecheck   # pyright
make test        # pytest with coverage
make build       # uv build
```

Run lint, typecheck and tests before finishing a change; CI runs all of them.

## Conventions

- Add new dependencies with `uv add` (runtime) or `uv add --group dev`; commit `uv.lock`.
- Configuration goes through `Settings`; do not read `os.environ` directly. Add new variables to `template.env`.
- Code must pass pyright in `standard` mode and ruff (rules in `pyproject.toml`). No `print` in library code.
- New behaviour needs tests.

## Engineering principles

- **KISS**: choose the simplest solution that works; no speculative abstractions.
- **SOLID**: single-purpose modules and functions, depend on abstractions, extend rather than modify, when that keeps code simpler. KISS wins on conflict.
- Keep changes small and match the surrounding style.
