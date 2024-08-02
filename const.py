import enum


APP_URL = "https://qa-scooter.praktikum-services.ru"
API_URI = f"{APP_URL}/api/v1"


class Endpoints:
    courier = "courier"
    courier_login = f"{courier}/login"

    orders = "orders"
    orders_accept = f"{orders}/accept"
    orders_cancel = f"{orders}/cancel"
    orders_finish = f"{orders}/finish"
    orders_track = f"{orders}/track"


class ResponseStatus(enum.IntEnum):
    OK = 200
    CREATED = 201

    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409

    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503


class ResponseMessage:
    OK = '{"ok":true}'
    LOGIN_NOT_FOUND = '{"code":404,"message":"Учетная запись не найдена"}'
    NOT_ENOUGH_DATA_FOR_LOGIN = '{"code":400,"message":"Недостаточно данных для входа"}'
    DELETE_NO_NOTFOUND = '{"code":404,"message":"Курьера с таким id нет."}'


class TestConstants:
    rent_periods = [
        "сутки",
        "двое суток",
        "трое суток",
        "четверо суток",
        "пятеро суток",
        "шестеро суток",
        "семеро суток",
    ]

    metro_stations = [
        "Сокольники",
        "Красносельская",
        "Комсомольская",
        "Чистые пруды",
        "Университет",
        "Юго-Западная",
    ]

    scooter_colors = ["black", "grey"]

    password = "P@ssw0rd"
    nonexistent_courier_id = 1
    order_list_params = {"limit": 10, "page": 0}
