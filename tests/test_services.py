import json

import pytest
import requests

from helpers.pet_service import get_pet, get_store_inventory, post_order


def test_get_pet():
    assert get_pet()[0]['id'] == 1010


def test_get_store_inventory():
    response = get_store_inventory()
    assert response['3000'] == 1
    assert response['5000'] == 1
    assert response['pending'] == 39


def test_post_order():
    body = {
        "id": 1,
        "petId": 1,
        "quantity": 0,
        "shipDate": "2024-02-17T09:42:10.119Z",
        "status": "placed",
        "complete": 'true'
    }
    response = post_order(body)

    assert response['id'] == body['id']
    assert response['status'] == body['status']



