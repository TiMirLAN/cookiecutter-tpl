#!/usr/bin/env bash

git init

poetry init
poetry add -D pre-commit isort black flake8 mypy
poetry run pre-commit install


{% if cookiecutter.install_sentry == "y" %}
poetry add sentry-sdk
{% endif %}

{% if cookiecutter.install_loguru == "y" %}
poetry add loguru
{% endif %}

git add -A
git commit -am "initial"
