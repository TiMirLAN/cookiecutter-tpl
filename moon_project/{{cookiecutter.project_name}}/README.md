# {{ cookiecutter.project_name }}

Monorepo managed by [moon](https://moonrepo.dev) with tools pinned by
[proto](https://moonrepo.dev/proto) in `.prototools`.

## Tech stack

| Area | Tool |
| --- | --- |
| Monorepo task runner | [moon](https://moonrepo.dev) |
| Toolchain manager | [proto](https://moonrepo.dev/proto) (versions in `.prototools`) |
| Python packaging | [uv](https://docs.astral.sh/uv/) |
| Python lint and format | [ruff](https://docs.astral.sh/ruff/) |
| Python tests | [pytest](https://docs.pytest.org) |
| CI | GitHub Actions via `moonrepo/setup-toolchain` and `moon ci` |

Python {{ cookiecutter.python_version }}+ is the baseline for Python projects.

## Getting started

```bash
proto use              # install pinned moon and uv
cp example.env .env    # local configuration
moon run :setup        # install dependencies of every project
```

## Commands

- `moon run :lint` / `moon run :test` — run for all projects
- `moon run <project>:dev` — start a project in dev mode
- `moon ci` — what CI runs

## Layout

```
apps/        deployable applications (one moon project each)
packages/    shared libraries
.moon/       moon workspace configuration
.prototools  pinned tool versions
```

Projects are discovered from `apps/*` and `packages/*`; each needs a `moon.yml`.
