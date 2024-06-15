import requests
import allure
import json
from data import URLs


class UserMethods:
    @staticmethod
    @allure.step("Отправка POST на  register")
    def create_user(payload):
        response = requests.post(URLs.REGISTER_URL, data=payload)
        return response

    @staticmethod
    @allure.step("Отправка DELETE на auth/user")
    def delete_user(access_token):
        return requests.delete(URLs.USER_URL, headers={'Authorization': access_token})

    @staticmethod
    @allure.step("Отправка POST на auth/login")
    def login_user(payload):
        response = requests.post(URLs.LOGIN_URL, data=payload)
        return response

    @staticmethod
    @allure.step("Отправка PATCH на auth/user")
    def patch_user(payload, access_token):
        response = requests.patch(URLs.USER_URL, data=payload, headers={'Authorization': access_token})
        return response


class OrderMethods:
    @staticmethod
    @allure.step("Отправка  GET на ingredients")
    def get_ingredients():
        response = requests.get(URLs.INGREDIENTS_URL)
        return response.json()['data']

    @staticmethod
    @allure.step("Отправка POST на orders")
    def create_order(body, access_token):
        response = requests.post(URLs.ORDERS_URL,
                                 json={"ingredients": body},
                                 headers={'Authorization': access_token})
        return response

    @allure.step("Отправка  GET на orders с юзером")
    def get_orders_by_user(access_token):
        response = requests.get(URLs.ORDERS_URL, headers={'Authorization': access_token})
        return response
