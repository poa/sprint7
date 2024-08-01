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