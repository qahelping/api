import pytest

from helpers.get_data import get_data_from_json

data = get_data_from_json("../files/file.json")

@pytest.mark.parametrize("data", data)
def test_json(data):
    print(data)
    assert data['name'] in ('Dominator', 'TheKiller', 'Vasya666', 'Cheater')
