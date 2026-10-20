#!/usr/bin/env python
import os
import shutil
import subprocess
import sys
from pathlib import Path

GIT_INIT = "{{ cookiecutter.git_init }}" == "y"
INCLUDE_EXAMPLE_APP = "{{ cookiecutter.include_example_app }}" == "y"


def run(*command: str) -> bool:
    """Run a command in the project dir; report failure instead of aborting."""
    try:
        subprocess.run(command, check=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"warning: `{' '.join(command)}` failed: {exc}", file=sys.stderr)
        return False
    return True


def remove_example_app() -> None:
    shutil.rmtree(Path("apps") / "example")


def setup_tools() -> None:
    if os.environ.get("COOKIECUTTER_SKIP_TOOLS"):
        return
    if shutil.which("proto"):
        run("proto", "use")
    else:
        print("proto not found, skipping `proto use`", file=sys.stderr)
    if shutil.which("moon"):
        run("moon", "sync", "projects")
    else:
        print("moon not found, skipping `moon sync`", file=sys.stderr)


def setup_git() -> None:
    run("git", "init", "-b", "master")


def commit() -> None:
    if run("git", "add", "-A"):
        run("git", "commit", "-m", "initial")


if __name__ == "__main__":
    if not INCLUDE_EXAMPLE_APP:
        remove_example_app()
    if GIT_INIT:
        setup_git()
    setup_tools()
    if GIT_INIT:
        commit()
