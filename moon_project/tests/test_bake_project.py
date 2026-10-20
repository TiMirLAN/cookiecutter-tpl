import shutil
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
import yaml

if TYPE_CHECKING:
    from pytest_cookies.plugin import Cookies


@pytest.fixture(autouse=True)
def skip_tools(monkeypatch: pytest.MonkeyPatch) -> None:
    """Never run `proto use` / `moon sync` while baking."""
    monkeypatch.setenv("COOKIECUTTER_SKIP_TOOLS", "1")
    monkeypatch.setenv("GIT_AUTHOR_NAME", "Test")
    monkeypatch.setenv("GIT_AUTHOR_EMAIL", "test@example.com")
    monkeypatch.setenv("GIT_COMMITTER_NAME", "Test")
    monkeypatch.setenv("GIT_COMMITTER_EMAIL", "test@example.com")


def git(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=path, capture_output=True, text=True, check=False
    )


def test_bakes_expected_files(cookies: "Cookies") -> None:
    result = cookies.bake()
    assert result.exit_code == 0, result.exception
    path = result.project_path
    for name in (
        ".editorconfig",
        ".gitignore",
        ".prototools",
        ".moon/workspace.yml",
        ".github/workflows/ci.yml",
        "example.env",
        "README.md",
        "apps/example/moon.yml",
        "apps/example/pyproject.toml",
        "packages",
    ):
        assert (path / name).exists(), name


def test_no_unrendered_jinja(cookies: "Cookies") -> None:
    result = cookies.bake()
    assert result.exit_code == 0, result.exception
    for file in result.project_path.rglob("*"):
        if file.is_file() and ".git" not in file.relative_to(result.project_path).parts:
            text = file.read_text()
            assert "{{" not in text and "{%" not in text, file
            assert "{{" not in str(file.relative_to(result.project_path))


def test_git_init_yes(cookies: "Cookies") -> None:
    result = cookies.bake(extra_context={"git_init": "y"})
    assert result.exit_code == 0, result.exception
    assert (result.project_path / ".git").is_dir()
    log = git(result.project_path, "log", "--format=%s")
    assert log.stdout.strip() == "initial", log.stderr
    assert git(result.project_path, "status", "--porcelain").stdout == ""


def test_git_init_no(cookies: "Cookies") -> None:
    result = cookies.bake(extra_context={"git_init": "n"})
    assert result.exit_code == 0, result.exception
    assert not (result.project_path / ".git").exists()


def test_without_example_app(cookies: "Cookies") -> None:
    result = cookies.bake(extra_context={"include_example_app": "n"})
    assert result.exit_code == 0, result.exception
    assert not (result.project_path / "apps" / "example").exists()
    assert (result.project_path / "apps").is_dir()


def test_gitignore_keeps_example_env(cookies: "Cookies") -> None:
    result = cookies.bake(extra_context={"git_init": "y"})
    assert result.exit_code == 0, result.exception
    path = result.project_path
    assert git(path, "check-ignore", ".env").returncode == 0
    assert git(path, "check-ignore", "example.env").returncode == 1
    assert git(path, "ls-files", "example.env").stdout.strip() == "example.env"


def test_yaml_is_valid(cookies: "Cookies") -> None:
    result = cookies.bake()
    assert result.exit_code == 0, result.exception
    path = result.project_path
    workspace = yaml.safe_load((path / ".moon/workspace.yml").read_text())
    assert workspace["projects"] == ["apps/*", "packages/*"]
    project = yaml.safe_load((path / "apps/example/moon.yml").read_text())
    assert {"setup", "dev", "test", "lint"} <= set(project["tasks"])
    yaml.safe_load((path / ".github/workflows/ci.yml").read_text())


@pytest.mark.skipif(shutil.which("uv") is None, reason="uv is not installed")
def test_example_app_tests_pass(cookies: "Cookies") -> None:
    result = cookies.bake(extra_context={"git_init": "n"})
    assert result.exit_code == 0, result.exception
    app = result.project_path / "apps" / "example"
    for command in (
        ["uv", "run", "pytest", "-q"],
        ["uv", "run", "ruff", "check", "."],
        ["uv", "run", "ruff", "format", "--check", "."],
    ):
        proc = subprocess.run(
            command, cwd=app, capture_output=True, text=True, check=False
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr


@pytest.mark.skipif(shutil.which("moon") is None, reason="moon is not installed")
def test_moon_sees_example_project(cookies: "Cookies") -> None:
    result = cookies.bake(extra_context={"git_init": "y"})
    assert result.exit_code == 0, result.exception
    proc = subprocess.run(
        ["moon", "query", "projects"],
        cwd=result.project_path,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "example" in proc.stdout
