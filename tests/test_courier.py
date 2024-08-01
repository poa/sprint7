import pytest

from api.courier import CourierAPI
from const import ResponseStatus as RS


def test_courier_create_complete_courier_data(test_data):
    print(test_data.courier.precreated)
    # with (CourierAPI(*test_data.courier.existing_courier) as courier):
    #     assert (
    #         courier.is_registered is True and
    #         courier.last_status == RS.CREATED
    #     )
    pass


def test_courier_create_negative():
    pass


def test_courier_create_existing():
    pass


def test_courier_login_positive():
    pass    


def test_courier_login_negative():
    pass
