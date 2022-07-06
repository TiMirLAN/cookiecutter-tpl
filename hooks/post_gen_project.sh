#!/usr/bin/env bash

git init

poetry install
poetry run pre-commit install

git add -A
git commit -am "initial"
