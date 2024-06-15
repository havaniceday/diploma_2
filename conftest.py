import allure
from helpers import SampleUserData
from api_methods import UserMethods
import pytest


@allure.step("Удаление пользователя")
@pytest.fixture(scope='function')
def delete_user():
    token_holder = {}
    yield token_holder
    access_token = token_holder.get('access_token')
    if access_token:
        UserMethods.delete_user(access_token)



@allure.step("Создание пользователя с удалением в конце теста")
@pytest.fixture(scope="function")
def create_user_with_deletion():
    user = SampleUserData.generate_new_user()
    response = UserMethods.create_user(user)
    access_token = response.json()['accessToken']
    yield user, access_token
    UserMethods.delete_user(access_token)
