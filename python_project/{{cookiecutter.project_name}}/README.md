# {{ cookiecutter.project_name }}

## Tech stack

| Area | Tool |
| --- | --- |
| Language | Python {{ cookiecutter.python_version }}+ |
| Packaging and environments | [uv](https://docs.astral.sh/uv/) with [hatchling](https://hatch.pypa.io) build backend |
| Settings | [pydantic](https://docs.pydantic.dev) / [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) (reads `.env`) |
{%- if cookiecutter.install_sentry == "y" %}
| Error tracking | [sentry-sdk](https://docs.sentry.io/platforms/python/) |
{%- endif %}
{%- if cookiecutter.install_loguru == "y" %}
| Logging | [loguru](https://loguru.readthedocs.io) |
{%- endif %}
| Lint and format | [ruff](https://docs.astral.sh/ruff/) |
| Type checking | [pyright](https://microsoft.github.io/pyright/) |
| Tests | [pytest](https://docs.pytest.org) with pytest-cov |
| Git hooks | [pre-commit](https://pre-commit.com) |
| CI and updates | GitHub Actions, Dependabot |

## Getting started

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
uv sync
uv run pre-commit install
cp template.env .env
```

## Commands

| Command | Description |
| --- | --- |
| `make sync` | Install dependencies |
| `make lint` | ruff check and format check |
| `make fmt` | Apply ruff fixes and formatting |
| `make typecheck` | Run pyright |
| `make test` | Run pytest with coverage |
| `make build` | Build sdist and wheel |

## Layout

```
src/{{ cookiecutter.project_slug }}/   package (typed, with settings.py)
tests/                                 pytest suite
.github/                               CI workflow and Dependabot
```
