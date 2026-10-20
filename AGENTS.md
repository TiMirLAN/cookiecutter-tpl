# AGENTS.md

Guidance for AI coding agents working in this repository.

## Instruction files

1. Read this file first.
2. Then read `LOCAL_AGENTS.md` in the same directory, if it exists. It describes the local development environment, is gitignored, and **takes priority over `AGENTS.md`** when they conflict.
3. Nested `AGENTS.md` / `LOCAL_AGENTS.md` files (for example in `python_project/`) apply to their subtree and refine this file.

Never commit `LOCAL_AGENTS.md`.

## Overview

A collection of Cookiecutter templates:

- `python_project/` — single typed Python package (uv, ruff, pyright, pytest, pre-commit)
- `moon_project/` — moon + proto monorepo with an optional Python example app

Each template directory contains `cookiecutter.json`, `hooks/`, a `{{cookiecutter.project_name}}/` directory (the generated project), `tests/`, and its own uv-managed dev environment.

## Commands

Run from inside a template directory (`python_project/` or `moon_project/`):

```bash
uv sync          # install dev dependencies
uv run pytest    # bake the template and verify the output
uv run ruff check . && uv run ruff format --check .
```

CI (`.github/workflows/tests.yml`) runs `uv run pytest` for every template.

## Conventions

- Files under `{{cookiecutter.project_name}}/` and the hooks are Jinja templates. Do not break `{{ ... }}` / `{% ... %}` syntax, and make sure no unrendered Jinja is left in baked output (tests check this).
- Hooks must be idempotent-friendly and fail soft where possible (see `moon_project/hooks/post_gen_project.py`).
- When changing a template, update its tests in `tests/test_bake_project.py` and the relevant README.
- Pinned tool versions (`.prototools`, pre-commit revs, CI actions) are deliberate; do not bump them unasked.
- Keep the root `README.md`, template READMEs and generated-project READMEs consistent with the code.

## Engineering principles

- **KISS**: choose the simplest solution that works. No speculative options, abstractions or configuration.
- **SOLID**: keep units single-purpose, depend on abstractions rather than concretions, and prefer extension over modification, where it keeps the code simpler rather than more elaborate. Where SOLID and KISS conflict, KISS wins.
- Keep changes small and focused; match the style of surrounding code.
