import pytest

from api.orders import OrdersAPI
from const import ResponseStatus as RS, ResponseMessage as RespMsg, TestConstants as TC


@pytest.mark.parametrize(
    "data_set",
    [
        "complete_set_no_color",
        "complete_set_black_color",
        "complete_set_grey_color",
        "complete_set_both_color",
    ],
)
def test_order_create(test_data, data_set):
    order_data = getattr(test_data.order, data_set)
    with OrdersAPI(*order_data) as order:
        print(f"\n{order_data}\n{order.last_status}: {order.last_msg}")
        assert (
            order.track is not None
            and order.last_status == RS.CREATED
            and order.last_msg.find("track") > 0
        )


def test_orders_list():
    pass
