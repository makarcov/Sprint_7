import requests
import random
import string
from faker import Faker

from data import CreateCourierData


class Helpers:
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
