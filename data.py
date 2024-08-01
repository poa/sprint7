from tools import DataGenerator


class CourierData:

    def __init__(self):
        data = DataGenerator()

        self.precreated = [data.login, data.password, data.first_name]

        data.new_name()
        self.complete = [data.login, data.password, data.first_name]

        self.no_password = [data.login, None, data.first_name]
        self.no_login = [None, data.password, data.first_name]
        self.no_name = [self.no_login, data.password, None]


class TestData:
    def __init__(self):
        self.courier = CourierData()
