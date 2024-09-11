import pytest

from scooter_api import ScooterApi


class TestGetOrdersList:

    def test_get_orders_list_success(self):
        get_orders_list_request = ScooterApi.get_orders_list()

        assert get_orders_list_request.status_code == 200 and "orders" in get_orders_list_request.text
