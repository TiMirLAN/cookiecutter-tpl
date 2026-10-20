# {{ cookiecutter.project_name }}

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
uv sync
uv run pre-commit install
```

Common tasks (see `Makefile`): `make lint`, `make fmt`, `make typecheck`, `make test`, `make build`.
