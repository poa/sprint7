import pytest

from data import TestData
from api.courier import CourierAPI

# form ya_scooter_api import


@pytest.fixture(scope='function')
def test_data():
    data = TestData()
    yield data


@pytest.fixture(scope="session")
def registered(test_data):
    registered_courier = CourierAPI(*test_data.courier.existing_courier)
    yield registered_courier
    registered_courier.delete()
