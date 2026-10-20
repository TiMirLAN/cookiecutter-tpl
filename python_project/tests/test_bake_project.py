import os
import shlex
import subprocess
from contextlib import contextmanager
from typing import TYPE_CHECKING

from cookiecutter.utils import rmtree

if TYPE_CHECKING:
    from pytest_cookies.plugin import Cookies, Result


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result: Result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_bakes_expected_files(cookies: "Cookies"):
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        path = result.project_path
        for name in ("pyproject.toml", "uv.lock", ".python-version", "Makefile"):
            assert (path / name).exists(), name
        slug = path.name.replace("-", "_")
        assert (path / "src" / slug / "py.typed").exists()
        assert not (path / ".flake8").exists()


def test_quality_checks_pass(cookies: "Cookies"):
    with bake_in_temp_dir(cookies) as result:
        for cmd in (
            "uv run ruff check .",
            "uv run ruff format --check .",
            "uv run pyright",
            "uv run pytest",
        ):
            assert run_inside_dir(cmd, result.project_path) == 0


def test_optional_dependencies(cookies: "Cookies"):
    extra = {"install_sentry": "y", "install_loguru": "y"}
    with bake_in_temp_dir(cookies, extra_context=extra) as result:
        pyproject = (result.project_path / "pyproject.toml").read_text()
        assert "sentry-sdk" in pyproject
        assert "loguru" in pyproject
