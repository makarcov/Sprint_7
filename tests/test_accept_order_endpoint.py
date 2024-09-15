import pytest
import allure

from data import CreateOrderData
from helpers import Helpers
from scooter_api import ScooterApi


class TestAcceptOrder:

    @allure.title('Тестируем функцию принятия заказа')
    @allure.description('Успешный запрос на приятие заказа возвращает {"ok":true} и код 200')
    def test_accept_order_success(self):
        courier_body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(courier_body)
        login_body = courier_body.copy()
        del login_body['firstName']
        login_request = ScooterApi.login_courier(login_body)
        courier_id = login_request.json()["id"]

        order_body = CreateOrderData.body.copy()
        order_body["color"] = ["GREY"]

        free_orders_list_request = ScooterApi.get_free_orders_list()
        order_id = free_orders_list_request.json()["orders"][0]["id"]

        accept_order_request = ScooterApi.accept_order(order_id, courier_id)

        assert accept_order_request.status_code == 200 and accept_order_request.text == '{"ok":true}'

    @allure.title('Тестируем функцию принятия заказа, если передать неверный номер заказа')
    @allure.description('Запрос должен вернуть ошибку и код 404')
    def test_accept_order_with_wrong_order_id_failed(self):
        courier_body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(courier_body)
        login_body = courier_body.copy()
        del login_body['firstName']
        login_request = ScooterApi.login_courier(login_body)
        courier_id = login_request.json()["id"]

        order_body = CreateOrderData.body.copy()
        order_body["color"] = ["GREY"]

        order_id = 0000

        accept_order_request = ScooterApi.accept_order(order_id, courier_id)

        assert accept_order_request.status_code == 404 and accept_order_request.text == '{"code":404,"message":"Заказа с таким id не существует"}'

    @allure.title('Тестируем функцию принятия заказа, если номер заказа отсутсвует')
    @allure.description('Запрос должен вернуть ошибку и код 400')
    def test_accept_order_without_order_id_failed(self):
        courier_body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(courier_body)
        login_body = courier_body.copy()
        del login_body['firstName']
        login_request = ScooterApi.login_courier(login_body)
        courier_id = login_request.json()["id"]

        order_body = CreateOrderData.body.copy()
        order_body["color"] = ["GREY"]

        order_id = ''

        accept_order_request = ScooterApi.accept_order(order_id, courier_id)
        check = accept_order_request.url
        assert accept_order_request.status_code == 400 and accept_order_request.text == '{"code":400,"message":"Недостаточно данных для поиска"}'

    @allure.title('Тестируем функцию принятия заказа, если передать неверный id курьера')
    @allure.description('Запрос должен вернуть ошибку и код 404')
    def test_accept_order_with_wrong_courier_id_failed(self):
        courier_id = 0000

        order_body = CreateOrderData.body.copy()
        order_body["color"] = ["GREY"]

        free_orders_list_request = ScooterApi.get_free_orders_list()
        order_id = free_orders_list_request.json()["orders"][0]["id"]
        accept_order_request = ScooterApi.accept_order(order_id, courier_id)

        assert accept_order_request.status_code == 404 and accept_order_request.text == '{"code":404,"message":"Курьера с таким id не существует"}'

    @allure.title('Тестируем функцию принятия заказа, если id курьера отсутвует')
    @allure.description('Запрос должен вернуть ошибку и код 400')
    def test_accept_order_without_courier_id_failed(self):
        courier_id = ""

        order_body = CreateOrderData.body.copy()
        order_body["color"] = ["GREY"]

        free_orders_list_request = ScooterApi.get_free_orders_list()
        order_id = free_orders_list_request.json()["orders"][0]["id"]
        accept_order_request = ScooterApi.accept_order(order_id, courier_id)

        assert accept_order_request.status_code == 400 and accept_order_request.text == '{"code":400,"message":"Недостаточно данных для поиска"}'