import requests

from const import (
    API_URI,
    Endpoints as EP,
    ResponseStatus as RS,
)


class CourierAPI:
    def __init__(self, login=None, password=None, first_name=None):
        self.id = None
        self.is_registered = False
        resp = self.create_courier(login, password, first_name)
        self.last_status = resp.status_code
        self.last_msg = resp.text
        if self.last_status == RS.CREATED:
            self.login = login
            self.password = password
            self.first_name = first_name
            self.is_registered = True

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self.id is not None:
            CourierAPI.delete_by_id(self.id)
        else:
            self.delete_by_login()

    @staticmethod
    def get_payload(login=None, password=None, first_name=None):
        pl = {}
        if login is not None:
            pl["login"] = login
        if password is not None:
            pl["password"] = password
        if first_name is not None:
            pl["firstName"] = first_name

        return pl

    @staticmethod
    def create_courier(login, password, first_name):
        url = f"{API_URI}/{EP.courier}"
        payload = CourierAPI.get_payload(login, password, first_name)
        resp = requests.post(url, json=payload)
        return resp

    @staticmethod
    def login_courier(login, password):
        url = f"{API_URI}/{EP.courier_login}"
        payload = CourierAPI.get_payload(login, password)
        resp = requests.post(url, json=payload)
        return resp

    @staticmethod
    def delete_by_id(courier_id):
        url = f"{API_URI}/{EP.courier}/{courier_id}"
        resp = requests.delete(url)
        return resp

    def delete(self):
        if self.is_registered:
            resp = CourierAPI.login_courier(self.login, self.password)
            if resp.status_code == RS.OK:
                resp = CourierAPI.delete_by_id(self.id)
                return resp
