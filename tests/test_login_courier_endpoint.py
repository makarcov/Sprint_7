import pytest
import allure

from helpers import Helpers
from scooter_api import ScooterApi


class TestLoginCourier:

    @allure.title('Тестируем авторизацию курьера в системе')
    @allure.description('Запрос должен вернуть id курьера и код 200')
    def test_login_courier_success(self):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        login_body = body.copy()
        del login_body['firstName']
        login_request = ScooterApi.login_courier(login_body)

        assert login_request.status_code == 200 and "id" in login_request.text

    @allure.title('Тестируем авторизацию курьера в системе при передаче пустого обязательного поля')
    @allure.description('Запрос должен вернуть ошибку и код 400')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_login_courier_with_empty_field_failed(self, key):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        login_body = body.copy()
        del login_body['firstName']
        login_body[key] = ""
        login_request = ScooterApi.login_courier(login_body)
        expected_text = '{"code":400,"message":"Недостаточно данных для входа"}'

        assert login_request.status_code == 400 and login_request.text == expected_text, f'Can\'t login without {key}, status_code - {login_request.status_code}'

    @allure.title('Тестируем авторизацию курьера в системе при передаче несуществующей пары логин-пароль')
    @allure.description('Запрос должен вернуть ошибку и код 404')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_login_non_exist_courier_failed(self, key):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        login_body = body.copy()
        del login_body['firstName']
        login_body[key] = body[key] + '1'
        login_request = ScooterApi.login_courier(login_body)

        assert login_request.status_code == 404 and login_request.text == '{"code":404,"message":"Учетная запись не найдена"}'
