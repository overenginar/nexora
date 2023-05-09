import pytest


def pytest_addoption(parser):
    parser.addoption("--param", action="store")


@pytest.fixture(scope="session")
def param(request):
    param_value = request.config.option.param
    if param_value is None:
        pytest.skip()
    return param_value
