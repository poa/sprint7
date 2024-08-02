import allure
import pytest

from api.orders import OrdersAPI
from const import ResponseStatus as RS, TestConstants as TC

allure.dynamic.suite("Тесты API для заказов (orders)")


@pytest.mark.parametrize(
    "data_set",
    [
        "complete_set_no_color",
        "complete_set_black_color",
        "complete_set_grey_color",
        "complete_set_both_color",
    ],
)
def test_order_create_correct_data_successful(test_data, data_set):
    allure.dynamic.title(f"Создание заказа с полным набором данных: {data_set}. Ожидаем успех")
    order_data = getattr(test_data.order, data_set)
    with OrdersAPI(*order_data) as order:
        print(f"\n{order_data}\n{order.last_status}: {order.last_msg}")
        assert (
            order.track is not None
            and order.last_status == RS.CREATED
            and order.last_msg.find("track") > 0
        )


@allure.title("Получение списка заказов с ограничением по кол-ву. Ожидаем успех")
def test_orders_list_with_limit():
    resp = OrdersAPI.get_orders(TC.order_list_params)
    orders = resp.json()["orders"]
    print(f"\n{resp.status_code}: {len(orders)}")
    assert resp.status_code == RS.OK and len(orders) == TC.order_list_params["limit"]
