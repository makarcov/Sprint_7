import pytest
import allure

from scooter_api import ScooterApi


class TestGetOrdersList:

    @allure.title('Тестируем получение списка заказов')
    @allure.description('Запрос должен вернуть список заказов и код 200')
    def test_get_orders_list_success(self):
        get_orders_list_request = ScooterApi.get_orders_list()

        assert get_orders_list_request.status_code == 200 and "orders" in get_orders_list_request.text
