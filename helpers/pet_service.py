from helpers.base_service import get, post

BASE_URL = 'https://petstore.swagger.io/v2/'


def get_pet():
    url = BASE_URL + 'pet/findByStatus?status=pending'
    return get(url)


def get_store_inventory():
    url = BASE_URL + 'store/inventory'
    return get(url)

def post_order(body):
    url = BASE_URL + 'store/order'
    return post(url, body)
