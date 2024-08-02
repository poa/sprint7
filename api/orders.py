import allure
import requests

from const import (
    API_URI,
    Endpoints as EP,
    ResponseStatus as RS,
)


class OrdersAPI:
    def __init__(
        self,
        first_name=None,
        last_name=None,
        address=None,
        metro_station=None,
        phone=None,
        rent_time=None,
        delivery_date=None,
        comment=None,
        color=(),
    ):
        self.track = None
        self.is_accepted = False
        create_payload = self.create_payload(
            first_name,
            last_name,
            address,
            metro_station,
            phone,
            rent_time,
            delivery_date,
            comment,
            color,
        )
        resp = self.create_order(create_payload)
        self.last_status = resp.status_code
        self.last_msg = resp.text
        if self.last_status == RS.CREATED:
            self.track = resp.json()["track"]
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.cancel(self.track)
        pass

    @staticmethod
    def create_payload(
        first_name=None,
        last_name=None,
        address=None,
        metro_station=None,
        phone=None,
        rent_time=None,
        delivery_date=None,
        comment=None,
        color=None,
    ):
        payload = {
            "firstName": first_name if first_name is not None else "",
            "lastName": last_name if last_name is not None else "",
            "address": address if address is not None else "",
            "metroStation": metro_station if metro_station is not None else "",
            "phone": phone if phone is not None else "",
            "rentTime": rent_time if rent_time is not None else "",
            "deliveryDate": delivery_date if delivery_date is not None else "",
            "comment": comment if comment is not None else "",
            "color": color if color is not None else (),
        }
        if color is not None:
            if isinstance(color, tuple):
                payload["color"] = color
            else:
                payload["color"] = tuple(color)
        else:
            payload["color"] = ()

        return payload

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        url = f"{API_URI}/{EP.orders}"
        resp = requests.post(url, json=payload)
        return resp

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders(params=None):
        url = f"{API_URI}/{EP.orders}"
        resp = requests.get(url, params=params)
        return resp

    @staticmethod
    @allure.step("Отмена заказа")
    def cancel(track_id):
        # `cancel` endpoint doesn't work as described in API doc
        # and there is no any `delete` endpoint
        pass
