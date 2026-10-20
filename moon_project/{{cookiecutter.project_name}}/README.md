# {{ cookiecutter.project_name }}

Monorepo managed by [moon](https://moonrepo.dev) with tools pinned by
[proto](https://moonrepo.dev/proto) in `.prototools`.

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

Projects live in `apps/*` and `packages/*`.
