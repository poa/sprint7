import enum


APP_URL = "https://qa-scooter.praktikum-services.ru"
API_URI = f"{APP_URL}/api/v1"


class Endpoints:
    COURIER = "courier"
    COURIER_LOGIN = f"{COURIER}/login"

    ORDERS = "orders"
    ORDERS_ACCEPT = f"{ORDERS}/accept"
    ORDERS_CANCEL = f"{ORDERS}/cancel"
    ORDERS_FINISH = f"{ORDERS}/finish"
    ORDERS_TRACK = f"{ORDERS}/track"


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
    RENT_PERIODS = [
        "сутки",
        "двое суток",
        "трое суток",
        "четверо суток",
        "пятеро суток",
        "шестеро суток",
        "семеро суток",
    ]

    METRO_STATIONS = [
        "Сокольники",
        "Красносельская",
        "Комсомольская",
        "Чистые пруды",
        "Университет",
        "Юго-Западная",
    ]

    SCOOTER_COLORS = ["black", "grey"]

    PASSWORD = "P@ssw0rd"
    NONEXISTENT_COURIER_ID = 1
    ORDER_LIST_PARAMS = {"limit": 10, "page": 0}
