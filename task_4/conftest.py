
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru"
    )
    parser.addoption(
        "--status_code",
        default=200,

    )
    parser.addoption(
        "--status_code_error",
        default=404,

    )
@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture()
def error_status_code(request):
    return request.config.getoption("--error_status_code")
