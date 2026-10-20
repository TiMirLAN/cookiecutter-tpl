# moon_project

Cookiecutter template for a monorepo managed by [moon](https://moonrepo.dev), with toolchain versions pinned by [proto](https://moonrepo.dev/proto).

## Usage

```bash
uvx cookiecutter gh:<owner>/cookiecutter-tpl --directory moon_project
```

## Variables

| Variable | Default | Description |
| --- | --- | --- |
| `full_name` | `cookiecutter-tpl-moon-project` | Human-readable name |
| `project_name` | derived from `full_name` | Lowercased, dash-separated; used as directory name |
| `project_slug` | derived from `project_name` | Importable name (dashes become underscores) |
| `author` | `Tim Mironov <...>` | `Name <email>`; the name is used as moon project owner |
| `python_version` | `3.13` | Minimum Python for the example app |
| `include_example_app` | `y` | `n` removes `apps/example` |
| `git_init` | `y` | `y` runs `git init -b master` and creates an `initial` commit |

## What you get

- `.moon/workspace.yml` with projects discovered in `apps/*` and `packages/*`
- `.prototools` pinning moon and uv
- `apps/example`: Python app (uv, pytest, ruff) with `setup`, `dev`, `test`, `lint` moon tasks
- GitHub Actions CI running `moon ci`
- `.editorconfig`, `.gitignore`, `example.env`

See the generated project's README for its tech stack.

## Post-generation hook

`hooks/post_gen_project.py`:

1. removes `apps/example` if `include_example_app` is `n`
2. runs `git init -b master` if `git_init` is `y`
3. runs `proto use` and `moon sync projects` when those tools are installed (skipped with a warning otherwise, or entirely if `COOKIECUTTER_SKIP_TOOLS` is set)
4. creates the `initial` commit

## Testing the template

```bash
uv sync
uv run pytest
```

Tests bake the template with `pytest-cookies` (with `COOKIECUTTER_SKIP_TOOLS=1`). Tests needing `uv` or `moon` are skipped when those are not installed.
