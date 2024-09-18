import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--env",  # Имя параметра
        action="store",  # Как хранить значение (можно store_true/store_false для флагов)
        default="dev",  # Значение по умолчанию, если параметр не передан
        help="Environment to run tests against"  # Описание опции
    )

    parser.addoption(
        "--domen",
        default="org",
        help="Domen for endpoints"
    )


    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def domen(request):
    return request.config.getoption("--domen")

@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))