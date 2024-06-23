import allure
import pytest
from api_methods import UserMethods
from data import Responses


class TestChangeUserData:
    @allure.title('Успешное изменение данных пользователя, {field}')
    @allure.description('При успешном изменении {field} возвращает HTTP 200 и email')
    @pytest.mark.parametrize("field", ['email', 'password', 'name'])
    def test_change_user_data_success(self, field, create_user_with_deletion):
        user_data, access_token = create_user_with_deletion
        UserMethods.login_user(user_data)
        user_data[field] = "abracadabra"
        response = UserMethods.patch_user(payload=user_data, access_token=access_token)
        assert response.status_code == 200 and response.json()['user']['email'] == user_data['email']

    @allure.title('Невозможность изменения данных неавторизованного пользователя, {field}')
    @allure.description('При попытке изменения возвращает HTTP 401 и сообщение об ошибке')
    @pytest.mark.parametrize("field", ['email', 'password', 'name'])
    def test_change_unauthorized_user_data_failure(self, field, create_user_with_deletion):
        user_data, access_token = create_user_with_deletion
        UserMethods.login_user(user_data)
        user_data[field] = "abracadabra"
        access_token_1 = ""
        response = UserMethods.patch_user(payload=user_data, access_token=access_token_1)
        assert (response.status_code == Responses.UNAUTHORIZED_USER['code']
                and response.json()['message'] == Responses.UNAUTHORIZED_USER['message'])