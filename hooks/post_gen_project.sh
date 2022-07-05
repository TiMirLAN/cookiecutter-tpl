#!/usr/bin/env bash

git init
git add -A
git commit -am "initial" --short

poetry install
poetry run pre-commit install
