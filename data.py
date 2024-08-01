from tools import DataGenerator
from const import TestConstants as TC


class CourierData:

    def __init__(self):
        data = DataGenerator()

        self.precreated = [data.login, TC.password, data.first_name]

        data.new_name()
        self.complete = [data.login, TC.password, data.first_name]

        self.no_password = [data.login, None, data.first_name]
        self.no_login = [None, TC.password, data.first_name]
        self.no_name = [data.login, TC.password, None]


class TestData:
    def __init__(self):
        self.courier = CourierData()
