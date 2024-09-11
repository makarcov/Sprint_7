import requests
import random
import string
from faker import Faker

from data import CreateCourierData


class Helpers:
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @staticmethod
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

    @staticmethod
    def generate_login():
        faker = Faker()
        return faker.user_name()

    @staticmethod
    def generate_password():
        faker = Faker()
        return faker.password(7)

    @staticmethod
    def generate_first_name():
        faker = Faker()
        return faker.first_name()

    @staticmethod
    def modify_create_courier_body():
        body = CreateCourierData.body.copy()
        body['login'] = Helpers.generate_login()
        body['password'] = Helpers.generate_password()
        body['firstName'] = Helpers.generate_first_name()

        return body
