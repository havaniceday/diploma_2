import random
from faker import Faker
import allure
import api_methods


class SampleUserData:

    @staticmethod
    def generate_new_user():
        fake = Faker()
        payload = dict(email=f'{fake.email()}', password=f'{random.randint(10000, 9999999999)}', name=fake.name())
        return payload

    @staticmethod
    def prepare_login_data(payload):
        del payload["name"]
        return payload

    @staticmethod
    @allure.step("Получить случайный ингредиент")
    def get_random_ingredient(count=1):
        ingredients = api_methods.OrderMethods.get_ingredients()
        payload = random.sample(set([i['_id'] for i in ingredients]), count)
        return payload
