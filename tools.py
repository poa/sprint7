from datetime import datetime, timedelta
from random import choice

from faker import Faker
from unidecode import unidecode as translit

from const import TestConstants as TC


class DataGenerator:
    def __init__(self):
        self.fake = Faker(["ru_RU"])
        self.address = ""
        self.email = ""
        self.name = ""
        self.first_name = ""
        self.last_name = ""
        self.login = ""
        self.password = ""
        self.phone = ""
        self.comment = ""
        self.date = ""
        self.metro_station = ""
        self.rent_period_text = ""
        self.rent_period_int = None
        self.scooter_color = ""

        self.new_address()
        self.new_email()
        self.new_name()
        self.new_password()
        self.new_phone()
        self.new_comment()
        self.new_date()
        self.new_metro_station()
        self.new_rent_period()
        self.new_scooter_color()

    def new_address(self):
        self.address = self.fake.street_address().replace("/", "")
        return self.address

    def new_name(self):
        self.first_name = self.fake.first_name_male().replace("-", "")
        self.last_name = self.fake.last_name_male().replace("-", "")
        self.name = self.first_name + " " + self.last_name
        self.login = translit(self.name).replace(" ","_").lower()
        return self.name

    def new_email(self):
        self.email = self.fake.email()
        return self.email

    def new_password(self):
        self.password = self.fake.password(length=8, special_chars=False)
        return self.password

    def new_phone(self):
        self.phone = "+7" + str(self.fake.random_number(10, True))
        return self.phone

    def new_comment(self):
        self.comment = self.fake.sentence()
        return self.comment

    def new_date(self):
        start_date = datetime.today()
        end_date = start_date + timedelta(days=7)
        self.date = self.fake.date_between(start_date, end_date).__str__()
        return self.date

    def new_metro_station(self):
        self.metro_station = choice(TC.metro_stations)
        return self.metro_station

    def new_rent_period(self):
        self.rent_period_text = choice(TC.rent_periods)
        self.rent_period_int = 1 + TC.rent_periods.index(self.rent_period_text)
        return self.rent_period_int

    def new_scooter_color(self):
        self.scooter_color = choice(TC.scooter_colors)
        return self.scooter_color
