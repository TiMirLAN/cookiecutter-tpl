from {{ cookiecutter.project_slug }}.settings import Settings, settings


def test_settings_instantiates() -> None:
    assert isinstance(settings, Settings)
