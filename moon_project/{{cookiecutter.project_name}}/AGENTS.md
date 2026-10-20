# AGENTS.md

Guidance for AI coding agents working on {{ cookiecutter.project_name }}.

## Instruction files

1. Read this file first.
2. Then read `LOCAL_AGENTS.md` in this directory, if it exists. It describes the local development environment, is gitignored, and **takes priority over `AGENTS.md`** when they conflict.
3. Each project under `apps/` or `packages/` may have its own `AGENTS.md` / `LOCAL_AGENTS.md`, which apply to that project and refine this file.

Never commit `LOCAL_AGENTS.md`.

## Overview

Monorepo managed by moon, with toolchain versions pinned by proto in `.prototools` (moon, uv). Python baseline is {{ cookiecutter.python_version }}.

- `apps/*` — deployable applications, one moon project each
- `packages/*` — shared libraries
- `.moon/workspace.yml` — workspace config; projects are discovered from `apps/*` and `packages/*`
- `example.env` — documented environment variables; copy to `.env` (gitignored)

Every project needs a `moon.yml` declaring its tasks (`setup`, `dev`, `test`, `lint`).

## Commands

```bash
proto use              # install pinned tools
moon run :setup        # install dependencies of every project
moon run :lint         # lint all projects
moon run :test         # test all projects
moon run <project>:dev # run one project
moon ci                # what CI runs
```

Run `moon run :lint :test` before finishing a change.

## Conventions

- Drive everything through moon tasks rather than ad-hoc commands, so CI and local runs match.
- Python projects use uv (`pyproject.toml` + `uv.lock`) and ruff; add dependencies with `uv add` inside the project directory.
- Bump tool versions only in `.prototools`.
- New projects follow `apps/example`: `moon.yml`, `pyproject.toml`, `src/`, `tests/`.

## Engineering principles

- **KISS**: choose the simplest solution that works; no speculative abstractions or shared packages before there are two users.
- **SOLID**: single-purpose modules and functions, depend on abstractions, extend rather than modify, when that keeps code simpler. KISS wins on conflict.
- Keep changes small and match the surrounding style.
