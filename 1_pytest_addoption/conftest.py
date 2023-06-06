import requests
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )

    parser.addoption(
        '--method',
        default='get',
        choicer=['get', 'post', 'put', 'path', 'delete'],
        help='method to execute'
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):

    return getattr(request, request.config.getoption("--method"))