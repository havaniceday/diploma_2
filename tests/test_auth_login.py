import allure
import pytest
from api_methods import UserMethods
from data import Responses
from helpers import SampleUserData


class TestLoginUser:
    @allure.title('Авторизация с логином и паролем существующего пользователя')
    @allure.description('При успешной авторизации возвращает HTTP 200 и email')
    def test_login_existing_user(self, create_user_with_deletion):
        user_data, _ = create_user_with_deletion
        user_data = SampleUserData.prepare_login_data(user_data)
        response = UserMethods.login_user(user_data)
        assert response.status_code == 200 and response.json()['user']['email'] == user_data['email']

    @allure.title('Авторизация с неверным логином или паролем')
    @allure.description('При неуспешной авторизации возвращает HTTP 401 и сообщение об ошибке')
    @pytest.mark.parametrize("field", ['email', 'password'])
    def test_login_wrong_email_or_pass(self, field, create_user_with_deletion):
        user_data, _ = create_user_with_deletion
        user_data = SampleUserData.prepare_login_data(user_data)
        user_data[field] = "abracadabra"
        response = UserMethods.login_user(user_data)
        assert response.status_code == Responses.INCORRECT_PASSWORD["code"] and response.json()['message'] == \
               Responses.INCORRECT_PASSWORD['message']
