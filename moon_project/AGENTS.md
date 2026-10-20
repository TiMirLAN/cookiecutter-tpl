# AGENTS.md — moon_project

Guidance for AI coding agents working on the `moon_project` Cookiecutter template. Applies on top of the root `AGENTS.md`.

## Instruction files

1. Read the root `AGENTS.md`, then this file.
2. Then read `LOCAL_AGENTS.md` (this directory, if present; also the root one). It describes the local environment, is gitignored, and **takes priority over `AGENTS.md`**.

## Layout

- `cookiecutter.json` — variables: `full_name`, `project_name`, `project_slug`, `author`, `python_version`, `include_example_app`, `git_init`
- `hooks/post_gen_project.py` — removes the example app if declined, `git init -b master`, runs `proto use` and `moon sync projects` when installed, creates the initial commit
- `{{cookiecutter.project_name}}/` — the generated monorepo (see its own `AGENTS.md`)
- `tests/test_bake_project.py` — bakes with `pytest-cookies` and checks the result
- `pyproject.toml`, `uv.lock` — dev environment for the template itself

## Commands

```bash
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
```

Tests set `COOKIECUTTER_SKIP_TOOLS=1` so the hook never runs `proto` or `moon`. Tests needing `uv` or `moon` are skipped when those are absent.

## Conventions

- The hook is a Jinja-rendered Python file; ruff ignores for it are configured in `pyproject.toml`. Hook steps must fail soft: warn and continue rather than abort baking.
- `.moon/workspace.yml` project globs are `apps/*` and `packages/*`; tests assert this.
- Tool versions in `.prototools` are pinned deliberately.

## Principles

Follow **KISS** and **SOLID** (KISS wins on conflict): keep hook functions small and single-purpose, and avoid speculative options.
