#!/usr/bin/env bash


on_int() {
    exit 1
}

trap on_int INT

git init

echo "{{cookiecutter.interactive_poetry}}"
poetry config virtualenvs.in-project true
poetry init\
    {% if cookiecutter.interactive_poetry != "y" %}-q\{% endif %}
    --author='{{ cookiecutter.author }}'\
    --dependency=pydantic\
    --dev-dependency=pre-commit\
    --dev-dependency=isort\
    --dev-dependency=black\
    --dev-dependency=flake8\
    --dev-dependency=mypy
poetry install
poetry run pre-commit install


{% if cookiecutter.install_sentry == "y" %}
poetry add sentry-sdk
{% endif %}

{% if cookiecutter.install_loguru == "y" %}
poetry add loguru
{% endif %}

git add -A
git commit -am "initial"
