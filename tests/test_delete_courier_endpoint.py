import pytest

from helpers import Helpers
from scooter_api import ScooterApi


class TestDeleteCourier:

    def test_delete_courier_success(self):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        login_body = body.copy()
        del login_body['firstName']
        login_request = ScooterApi.login_courier(login_body)
        courier_id = login_request.json()["id"]
        delete_courier_request = ScooterApi.delete_courier(courier_id)

        assert delete_courier_request.status_code == 200 and delete_courier_request.text == '{"ok":true}'

    def test_delete_courier_with_wrong_id_failed(self):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        login_body = body.copy()
        del login_body['firstName']
        courier_id = 0000
        delete_courier_request = ScooterApi.delete_courier(courier_id)

        assert delete_courier_request.status_code == 404 and delete_courier_request.text == '{"code":404,"message":"Курьера с таким id нет."}'

    def test_delete_courier_without_id_failed(self):
        body = Helpers.modify_create_courier_body()
        ScooterApi.create_courier(body)
        login_body = body.copy()
        del login_body['firstName']
        courier_id = ''
        delete_courier_request = ScooterApi.delete_courier(courier_id)

        assert delete_courier_request.status_code == 404 and delete_courier_request.text == '{"code":404,"message":"Not Found."}'
