from {{ cookiecutter.project_slug }}_example import greet


def test_greet() -> None:
    assert greet() == "Hello, world!"
    assert greet("moon") == "Hello, moon!"
