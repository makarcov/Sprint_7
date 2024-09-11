import pytest

from data import CreateOrderData
from scooter_api import ScooterApi


class TestGetOrderByNumber:

    def test_get_order_by_number_success(self):
        body = CreateOrderData.body.copy()
        body["color"] = ["BLACK"]
        create_order_request = ScooterApi.create_order(body)
        track_id = create_order_request.json()["track"]
        get_order_by_number_request = ScooterApi.get_order_by_number(track_id)

        assert get_order_by_number_request.status_code == 200 and get_order_by_number_request.json()["order"]["track"] == track_id

    def test_get_order_by_wrong_number_failed(self):
        track_id = 0000
        get_order_by_number_request = ScooterApi.get_order_by_number(track_id)

        assert get_order_by_number_request.status_code == 404 and get_order_by_number_request.text == '{"code":404,"message":"Заказ не найден"}'

    def test_get_order_without_number_failed(self):
        track_id = ""
        get_order_by_number_request = ScooterApi.get_order_by_number(track_id)

        assert get_order_by_number_request.status_code == 400 and get_order_by_number_request.text == '{"code":400,"message":"Недостаточно данных для поиска"}'