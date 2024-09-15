import pytest
import allure

from data import CreateOrderData
from scooter_api import ScooterApi


class TestGetOrderByNumber:

    @allure.title('Тестируем получение заказа по номеру')
    @allure.description('Запрос должен вернуть в теле ответа трэк номер заказа и код 200')
    def test_get_order_by_number_success(self):
        body = CreateOrderData.body.copy()
        body["color"] = ["BLACK"]
        create_order_request = ScooterApi.create_order(body)
        track_id = create_order_request.json()["track"]
        get_order_by_number_request = ScooterApi.get_order_by_number(track_id)

        assert get_order_by_number_request.status_code == 200 and get_order_by_number_request.json()["order"]["track"] == track_id

    @allure.title('Тестируем получение заказа по номеру - передаем несуществующий номер заказа')
    @allure.description('Запрос должен вернуть ошибку и код 404')
    def test_get_order_by_wrong_number_failed(self):
        track_id = 0000
        get_order_by_number_request = ScooterApi.get_order_by_number(track_id)

        assert get_order_by_number_request.status_code == 404 and get_order_by_number_request.text == '{"code":404,"message":"Заказ не найден"}'

    @allure.title('Тестируем получение заказа по номеру - номер не указываем')
    @allure.description('Запрос должен вернуть ошибку и код 400')
    def test_get_order_without_number_failed(self):
        track_id = ""
        get_order_by_number_request = ScooterApi.get_order_by_number(track_id)

        assert get_order_by_number_request.status_code == 400 and get_order_by_number_request.text == '{"code":400,"message":"Недостаточно данных для поиска"}'