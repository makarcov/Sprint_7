import requests

from urls import Url, Endpoint


class ScooterApi:

    @staticmethod
    def create_courier(body):
        return requests.post(Url.BASE_URL + Endpoint.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    def login_courier(body):
        return requests.post(Url.BASE_URL + Endpoint.LOGIN_COURIER_ENDPOINT, data=body)

    @staticmethod
    def create_order(body):
        return requests.post(Url.BASE_URL + Endpoint.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    def get_orders_list():
        return requests.get(Url.BASE_URL + Endpoint.GET_ORDERS_LIST_ENDPOINT)

    @staticmethod
    def delete_courier(id):
        return requests.delete(Url.BASE_URL + Endpoint.DELETE_COURIER_ENDPOINT + str(id))

    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(Url.BASE_URL + Endpoint.ACCEPT_ORDER_ENDPOINT + str(order_id), params={"courierId": str(courier_id)})

    @staticmethod
    def get_order_by_number(track_id):
        return requests.get(Url.BASE_URL + Endpoint.GET_ORDER_BY_NUMBER_ENDPOINT, params={"t": str(track_id)})

    @staticmethod
    def get_free_orders_list():
        return requests.get(Url.BASE_URL + Endpoint.GET_FREE_ORDERS_LIST_ENDPOINT)
