import requests

from data import API_URI
from data import Endpoints as EP


class CourierAPI:
    @staticmethod
    def create_courier():
        pass

    @staticmethod
    def login_courier():
        pass

    @staticmethod
    def delete_courier(courier):
        requests.delete(f"{API_URI}/{EP.courier}/{courier}")


class OrdersAPI:
    @staticmethod
    def create_order():
        pass

    @staticmethod
    def delete_order():
        pass

    @staticmethod
    def list_orders():
        pass
