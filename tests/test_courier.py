import pytest

from api.courier import CourierAPI
from const import (
    ResponseStatus as RS,
    ResponseMessage as RespMsg
)


def test_courier_create_complete_courier_data(test_data):
    with (CourierAPI(*test_data.courier.precreated) as courier):
        print(f"{test_data.courier.precreated}")

        assert (
            courier.is_registered is True and
            courier.last_status == RS.CREATED and
            courier.last_msg == RespMsg.OK
        )


def test_courier_create_negative():
    pass


def test_courier_create_existing():
    pass


def test_courier_login_positive():
    pass    


def test_courier_login_negative():
    pass
