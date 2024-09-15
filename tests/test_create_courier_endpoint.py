import pytest
import allure

from helpers import Helpers
from scooter_api import ScooterApi


class TestCreateCourier:

    @allure.title('Тестируем создание нового курьера')
    @allure.description('Запрос должен вернуть {"ok":true} и код 201')
    def test_create_courier_success(self):
        body = Helpers.modify_create_courier_body()
        create_request = ScooterApi.create_courier(body)
        expected_response_text = '{"ok":true}'

        assert create_request.status_code == 201 and create_request.text == expected_response_text

    @allure.title('Тестируем создание двух одинаковых курьеров')
    @allure.description('Запрос должен вернуть ошибку и код 409')
    def test_create_two_identical_couriers_failed(self):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        create_request = ScooterApi.create_courier(body)
        expected_response_text = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

        assert create_request.status_code == 409 and create_request.text == expected_response_text

    @allure.title('Тестируем создание курьера с незаполненным обязательным полем')
    @allure.description('Запрос должен вернуть ошибку и код 400')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_create_new_courier_with_empty_field_failed(self, key):
        body = Helpers.modify_create_courier_body()
        body[key] = ""
        create_request = ScooterApi.create_courier(body)
        expected_response_text = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

        assert create_request.status_code == 400 and create_request.text == expected_response_text
