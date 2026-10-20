#!/usr/bin/env bash
set -euo pipefail

on_int() {
    exit 1
}

trap on_int INT

git init
uv sync
uv run pre-commit install

git add -A
git commit -m "initial"
