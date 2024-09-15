import requests
import allure

from urls import Url, Endpoint


class ScooterApi:

    @staticmethod
    @allure.step('Создаем нового курьера')
    def create_courier(body):
        return requests.post(Url.BASE_URL + Endpoint.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    @allure.step('Авторизируем курьера в системе')
    def login_courier(body):
        return requests.post(Url.BASE_URL + Endpoint.LOGIN_COURIER_ENDPOINT, data=body)

    @staticmethod
    @allure.step('Создаем новый заказ')
    def create_order(body):
        return requests.post(Url.BASE_URL + Endpoint.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    @allure.step('Получаем список заказов')
    def get_orders_list():
        return requests.get(Url.BASE_URL + Endpoint.GET_ORDERS_LIST_ENDPOINT)

    @staticmethod
    @allure.step('Удаляем курьера')
    def delete_courier(id):
        return requests.delete(Url.BASE_URL + Endpoint.DELETE_COURIER_ENDPOINT + str(id))

    @staticmethod
    @allure.step('Принимаем заказ в работу')
    def accept_order(order_id, courier_id):
        return requests.put(Url.BASE_URL + Endpoint.ACCEPT_ORDER_ENDPOINT + str(order_id), params={"courierId": str(courier_id)})

    @staticmethod
    @allure.step('Получаем заказ по его номеру')
    def get_order_by_number(track_id):
        return requests.get(Url.BASE_URL + Endpoint.GET_ORDER_BY_NUMBER_ENDPOINT, params={"t": str(track_id)})

    @staticmethod
    @allure.step('Получаем список заказов, доступных к принятию')
    def get_free_orders_list():
        return requests.get(Url.BASE_URL + Endpoint.GET_FREE_ORDERS_LIST_ENDPOINT)

    @staticmethod
    @allure.step('Регистрируем нового курьера и возвращаем логин-пароль-имя')
    def register_new_courier_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass