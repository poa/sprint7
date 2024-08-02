import pytest

from data import TestData
from api.courier import CourierAPI

# form ya_scooter_api import


@pytest.fixture(scope='function')
def test_data():
    data = TestData()
    yield data


@pytest.fixture(scope='function')
def precreated_courier(test_data):
    with CourierAPI(*test_data.courier.precreated) as precreated_courier:
        yield precreated_courier
