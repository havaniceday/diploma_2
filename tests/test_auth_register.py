import allure
import pytest
import requests
from helpers import SampleUserData
from api_methods import UserMethods
from data import Responses


class TestAuthRegister:

    @allure.title('Создание нового пользователя')
    @allure.description('Успешный запрос создания пользователя возвращает HTTP 200 и токен')
    def test_register_user_correct_data_successful(self, delete_user):
        response = UserMethods.create_user(SampleUserData.generate_new_user())
        access_token = response.json()['accessToken']
        assert (response.status_code == requests.codes['ok'] and
                str(response.json()['accessToken']).startswith('Bearer'))
        delete_user['access_token'] = access_token


    @allure.title('Создание дубликата пользователя')
    @allure.description('При попытке создания пользователя возвращает HTTP 403 и соответствующее сообщение об ошибке')
    def test_register_duplicate_user_unsuccessful(self, delete_user):
        user = SampleUserData.generate_new_user()
        response = UserMethods.create_user(user)
        access_token = response.json()['accessToken']
        response = UserMethods.create_user(user)
        assert response.status_code == Responses.USER_ALREADY_EXISTS['code'] and response.json()['message'] == Responses.USER_ALREADY_EXISTS['message']
        delete_user['access_token'] = access_token

    @allure.title('Создание пользователя без поля {field}')
    @allure.description('При попытке создания пользователя без обязательного поля возвращает HTTP 403 и соответствующее сообщение об ошибке')
    @pytest.mark.parametrize("field", ['email', 'password', 'name'])
    def test_register_user_without_required_fields_unsuccessful(self, field):
        user = SampleUserData.generate_new_user()
        user[field] = ''
        response = UserMethods.create_user(user)
        assert (response.status_code == Responses.NO_REQUIRED_FIELDS_PROVIDED['code'] and
                response.json()['message'] == Responses.NO_REQUIRED_FIELDS_PROVIDED['message'])

