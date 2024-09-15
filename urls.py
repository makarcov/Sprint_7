class Url:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru'


class Endpoint:

    CREATE_COURIER_ENDPOINT = '/api/v1/courier'
    LOGIN_COURIER_ENDPOINT = '/api/v1/courier/login'
    CREATE_ORDER_ENDPOINT = '/api/v1/orders'
    GET_ORDERS_LIST_ENDPOINT = '/api/v1/orders'
    DELETE_COURIER_ENDPOINT = '/api/v1/courier/'
    ACCEPT_ORDER_ENDPOINT = '/api/v1/orders/accept/'
    GET_ORDER_BY_NUMBER_ENDPOINT = '/api/v1/orders/track'

    GET_FREE_ORDERS_LIST_ENDPOINT = '/api/v1/orders?limit=10&page=0'
