from const import TestConstants as TC
from tools import DataGenerator


class CourierData:

    def __init__(self):
        data = DataGenerator()

        self.precreated = [data.login, TC.PASSWORD, data.first_name]

        data.new_name()
        self.complete = [data.login, TC.PASSWORD, data.first_name]

        self.no_password = [data.login, None, data.first_name]
        self.no_login = [None, TC.PASSWORD, data.first_name]
        self.no_name = [data.login, TC.PASSWORD, None]


class OrderData:
    def __init__(self):
        data = DataGenerator()

        complete_set_base = [
            data.first_name,
            data.last_name,
            data.address,
            data.metro_station,
            data.phone,
            data.rent_period_int,
            data.date,
            data.comment,
        ]

        self.complete_set_no_color = complete_set_base + [None]
        self.complete_set_black_color = complete_set_base + [TC.SCOOTER_COLORS[0]]
        self.complete_set_grey_color = complete_set_base + [TC.SCOOTER_COLORS[1]]
        self.complete_set_both_color = complete_set_base + [TC.SCOOTER_COLORS]


class TestData:
    def __init__(self):
        self.courier = CourierData()
        self.order = OrderData()
