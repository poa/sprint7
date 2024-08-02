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
        self.delete()

    @staticmethod
    def get_payload(login=None, password=None, first_name=None):
        payload = {
            "login": login if login is not None else "",
            "password": password if password is not None else "",
            "firstName": first_name if first_name is not None else "",
        }

        return payload

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

    def do_login(self):
        resp = self.login_courier(self.login, self.password)
        self.last_status = resp.status_code
        self.last_msg = resp.text
        if self.last_status == RS.OK:
            self.id = resp.json()["id"]
            return True

        return False

    def delete(self):
        if self.is_registered:
            print(f"Deleting Courier: {self.login}")
            if self.id is None:
                result = self.do_login()
                if result is not True:
                    return False

            resp = self.delete_by_id(self.id)
            self.last_status = resp.status_code
            self.last_msg = resp.text

            if self.last_status == RS.OK:
                self.is_registered = False
                return True

            return False
