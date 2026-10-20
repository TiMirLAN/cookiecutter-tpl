# cookiecutter-tpl

Personal collection of [Cookiecutter](https://cookiecutter.readthedocs.io) templates.

| Template | Description |
| --- | --- |
| [`python_project`](python_project/) | Single Python package: uv, ruff, pyright, pytest, pre-commit, GitHub Actions |
| [`moon_project`](moon_project/) | Polyglot-ready monorepo: moon + proto, with an optional uv-based Python example app |

## Usage

```bash
uvx cookiecutter gh:<owner>/cookiecutter-tpl --directory python_project
uvx cookiecutter gh:<owner>/cookiecutter-tpl --directory moon_project
# or from a local checkout
uvx cookiecutter ./python_project
```

Each template prompts for its own variables; see the template README for details.

## Repository layout

```
.github/workflows/tests.yml   CI: bakes and tests every template
python_project/               template + its own tests and dev environment
moon_project/                 template + its own tests and dev environment
```

Each template directory has the same shape:

```
cookiecutter.json             prompts and defaults
hooks/                        post-generation hook
{{cookiecutter.project_name}}/ the generated project (with its own README template)
tests/                        pytest-cookies tests that bake and verify the template
pyproject.toml, uv.lock       dev environment for testing the template
```

## Developing the templates

Requires [uv](https://docs.astral.sh/uv/).

```bash
cd python_project   # or moon_project
uv sync
uv run pytest
```

CI (`.github/workflows/tests.yml`) runs the same tests for each template on every push and pull request.
