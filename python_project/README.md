# python_project

Cookiecutter template for a typed Python package with a `src/` layout, managed by uv.

## Usage

```bash
uvx cookiecutter gh:<owner>/cookiecutter-tpl --directory python_project
```

## Variables

| Variable | Default | Description |
| --- | --- | --- |
| `full_name` | `cookiecutter-tpl-python-project` | Human-readable name |
| `project_name` | derived from `full_name` | Lowercased, dash-separated; used as directory and distribution name |
| `project_slug` | derived from `project_name` | Importable package name (dashes become underscores) |
| `author` | `Tim Mironov <...>` | `Name <email>`; email is optional |
| `python_version` | `3.14` | Minimum Python; drives `requires-python`, ruff and pyright targets, `.python-version` |
| `install_sentry` | `n` | `y` adds `sentry-sdk` as a dependency |
| `install_loguru` | `n` | `y` adds `loguru` as a dependency |

## What you get

- `src/<slug>/` package with `py.typed` and a pydantic-settings `Settings` class
- `tests/` with pytest and coverage
- `Makefile` shortcuts, pre-commit config, GitHub Actions CI, Dependabot
- `.editorconfig`, `.gitignore`, `template.env`

See the generated project's README for its tech stack.

## Post-generation hook

`hooks/post_gen_project.sh` runs `git init`, `uv sync`, `uv run pre-commit install`, then creates an `initial` commit. It requires `git` and `uv` on `PATH`.

## Testing the template

```bash
uv sync
uv run pytest
```

Tests in `tests/test_bake_project.py` bake the template with `pytest-cookies` and check the output.
