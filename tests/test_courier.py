import allure
import pytest

from api.courier import CourierAPI
from const import ResponseStatus as RS, ResponseMessage as RespMsg, TestConstants as TC

allure.dynamic.suite("Тесты API для курьеров (courier)")


@allure.title("Создание курьера с полным набором корректных данных. Ожидаем успех")
def test_courier_create_complete_courier_data_successful(test_data):
    with CourierAPI(*test_data.courier.precreated) as courier:
        print(f"{test_data.courier.precreated}")

        assert (
            courier.is_registered is True
            and courier.last_status == RS.CREATED
            and courier.last_msg == RespMsg.OK
        )


@pytest.mark.parametrize("data_set", ["no_login", "no_password"])
def test_courier_create_incomplete_courier_data_failed(test_data, data_set):
    allure.dynamic.title(f"Создание курьера с неполным набором данных: {data_set}. Ожидаем ошибку")
    courier_data = getattr(test_data.courier, data_set)
    print(courier_data)
    with CourierAPI(*courier_data) as courier:
        assert courier.is_registered is False and courier.last_status == RS.BAD_REQUEST


@allure.title("Попытка создать пользователя с уже существующим login. Ожидаем ошибку")
def test_courier_create_existing_conflict(precreated_courier, test_data):
    print(f"{[precreated_courier.login, precreated_courier.password]}")
    with CourierAPI(*test_data.courier.precreated) as courier:
        assert courier.is_registered is False and courier.last_status == RS.CONFLICT


@allure.title("Авторизация для существующего пользователя. Данные для входа верны. Ожидаем успех")
def test_courier_login_existent_successful(precreated_courier):
    print(f"{[precreated_courier.login, precreated_courier.password]}")
    assert (
        precreated_courier.do_login() is True
        and precreated_courier.last_status == RS.OK
        and precreated_courier.last_msg.find("id") > 0
    )


@allure.title("Авторизация для существующего пользователя. Пароль пустой. Ожидаем ошибку")
def test_courier_login_empty_password_failed(precreated_courier):
    courier_data = [precreated_courier.login, ""]
    resp = CourierAPI.login_courier(*courier_data)
    print(courier_data, resp.status_code)
    assert resp.status_code == RS.BAD_REQUEST and resp.text == RespMsg.NOT_ENOUGH_DATA_FOR_LOGIN


@allure.title("Авторизация для существующего пользователя. Пароль неверный. Ожидаем ошибку")
def test_courier_login_wrong_password_not_found(precreated_courier):
    courier_data = [precreated_courier.login, "bad_password"]
    resp = CourierAPI.login_courier(*courier_data)
    print(courier_data, resp.status_code)
    assert resp.status_code == RS.NOT_FOUND and resp.text == RespMsg.LOGIN_NOT_FOUND


@allure.title("Авторизация для несуществующего пользователя. Ожидаем ошибку")
def test_courier_login_nonexistent_failed(test_data):
    courier_data = test_data.courier.complete[:2]
    resp = CourierAPI.login_courier(*courier_data)
    print(courier_data, resp.status_code)
    assert resp.status_code == RS.NOT_FOUND and resp.text == RespMsg.LOGIN_NOT_FOUND


@allure.title("Удаление существующего пользователя. Ожидаем успех")
def test_courier_delete_existent_successful(precreated_courier):
    print(f"{[precreated_courier.login, precreated_courier.password]}")
    assert (
        precreated_courier.delete() is True
        and precreated_courier.last_status == RS.OK
        and precreated_courier.last_msg == RespMsg.OK
    )


@allure.title("Удаление несуществующего пользователя. Ожидаем ошибку")
def test_courier_delete_nonexistent_failed():
    resp = CourierAPI.delete_by_id(TC.nonexistent_courier_id)
    print(f"id: {TC.nonexistent_courier_id}, status: {resp.status_code}")
    assert resp.status_code == RS.NOT_FOUND and resp.text == RespMsg.DELETE_NO_NOTFOUND
