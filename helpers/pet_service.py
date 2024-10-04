from models.data import Order
from helpers.base_service import BaseService

BASE_URL = 'https://petstore.swagger.io/v2/'


class PetService(BaseService):
    def get_pet(self):
        url = BASE_URL + 'pet/findByStatus?status=pending'
        return self.get(url)


    def get_store_inventory(self):
        url = BASE_URL + 'store/inventory'
        return self.get(url)

    def post_order(self, body):
        url = BASE_URL + 'store/order'
        response = self.post(url, body)
        model = Order(**response)
        return model
