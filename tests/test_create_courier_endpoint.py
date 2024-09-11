import pytest

from helpers import Helpers
from scooter_api import ScooterApi


class TestCreateCourier:

    def test_create_courier_success(self):
        body = Helpers.modify_create_courier_body()
        create_request = ScooterApi.create_courier(body)
        expected_response_text = '{"ok":true}'

        assert create_request.status_code == 201 and create_request.text == expected_response_text

    def test_create_two_identical_couriers_failed(self):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        create_request = ScooterApi.create_courier(body)
        expected_response_text = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

        assert create_request.status_code == 409 and create_request.text == expected_response_text

    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_create_new_courier_with_empty_field_failed(self, key):
        body = Helpers.modify_create_courier_body()
        body[key] = ""
        create_request = ScooterApi.create_courier(body)
        expected_response_text = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

        assert create_request.status_code == 400 and create_request.text == expected_response_text
