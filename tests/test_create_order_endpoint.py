import pytest
import allure

from data import CreateOrderData
from scooter_api import ScooterApi


class TestCreateOrder:

    @allure.title('Тестируем создание заказа при разных вариантах цвета самоката')
    @allure.description('Запрос должен вернуть трэк номер заказа и код 201')
    @pytest.mark.parametrize('colour', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_success(self, colour):
        body = CreateOrderData.body.copy()
        body["color"] = colour
        create_order_request = ScooterApi.create_order(body)

        assert create_order_request.status_code == 201 and "track" in create_order_request.text
