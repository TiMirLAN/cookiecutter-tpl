# AGENTS.md — python_project

Guidance for AI coding agents working on the `python_project` Cookiecutter template. Applies on top of the root `AGENTS.md`.

## Instruction files

1. Read the root `AGENTS.md`, then this file.
2. Then read `LOCAL_AGENTS.md` (this directory, if present; also the root one). It describes the local environment, is gitignored, and **takes priority over `AGENTS.md`**.

## Layout

- `cookiecutter.json` — variables: `full_name`, `project_name`, `project_slug`, `author`, `python_version`, `install_sentry`, `install_loguru`
- `hooks/post_gen_project.sh` — `git init`, `uv sync`, `pre-commit install`, initial commit
- `{{cookiecutter.project_name}}/` — the generated project (see its own `AGENTS.md`)
- `tests/test_bake_project.py` — bakes the template with `pytest-cookies` and checks the result
- `pyproject.toml`, `uv.lock` — dev environment for the template itself (not shipped to generated projects)

## Commands

```bash
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
```

The hook runs `git commit`, `uv sync` and `pre-commit install`, so tests need git identity set (CI sets `GIT_AUTHOR_*` / `GIT_COMMITTER_*`) and are slower than usual.

## Conventions

- Optional features (`install_sentry`, `install_loguru`) are Jinja conditionals in the generated `pyproject.toml` and README. Add tests for both values when adding a new option.
- Generated-project tooling (ruff, pyright, pytest, pre-commit) must stay mutually consistent: same Python target, same line length.
- Do not add dependencies to the generated project unless a variable gates them.

## Principles

Follow **KISS** and **SOLID** (KISS wins on conflict): the simplest template that works, single-purpose hooks and files, no speculative options.
