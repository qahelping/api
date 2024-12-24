import pytest
from allpairspy import AllPairs

from helpers.get_data import get_data_from_csv


def id_val(val):
    return val[0]

auth_endpoints = get_data_from_csv("../files/auth_endpoints.csv")

@pytest.mark.parametrize("data", auth_endpoints, ids=id_val)
def test_with_generator(data):
    assert data[0] == 'login'