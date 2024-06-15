import allure
import api_methods
import helpers
from data import Responses


class TestOrders:
    @allure.title('Создание заказа с авторизацией и случайным ингредиентом')
    @allure.description("Успешный запрос возвращает код 200 и значение 'success': True")
    def test_create_order_authorized_with_ingredients(self, create_user_with_deletion):
        user, access_token = create_user_with_deletion
        ingredients = helpers.SampleUserData.get_random_ingredient(2)
        response = api_methods.OrderMethods.create_order(ingredients, access_token)
        assert response.status_code == 200 and response.json().get('success') is True

    @allure.title('Создание заказа с авторизацией без ингредиентов')
    @allure.description("Неуспешный запрос возвращает код 400 и сообщение об ошибке")
    def test_create_order_authorized_without_ingredients(self, create_user_with_deletion):
        user, access_token = create_user_with_deletion
        ingredients = []
        response = api_methods.OrderMethods.create_order(ingredients, access_token)
        assert response.status_code == Responses.NO_INGREDIENTS_PROVIDED["code"]
        assert response.json()['message'] == Responses.NO_INGREDIENTS_PROVIDED['message']

    @allure.title('Создание заказа с авторизацией и неверным кодом ингредиентов')
    @allure.description("Неуспешный запрос возвращает код 500")
    def test_create_order_authorized_with_wrong_ingredients(self, create_user_with_deletion):
        user, access_token = create_user_with_deletion
        ingredients = helpers.SampleUserData.get_random_ingredient(2)
        ingredients.append("s2df$dfssd")
        response = api_methods.OrderMethods.create_order(ingredients, access_token)
        assert response.status_code == Responses.UNKNOWN_INGREDIENT_ID["code"]
        assert 'Internal Server Error' in response.text

#этот тест ожидаемо падает, т.к. тест написан согласно документации, а поведение не соответствует документации, есть баг
    @allure.title('Создание заказа без авторизации с ингредиентами')
    @allure.description("Запрос возвращает код 401 и сообщение об ошибке - тест написан по документации, ожидаемо падает, т.к. есть баг: заказ успешно создается без авторизации, чего быть не должно, по документации юзер должен быть переадресован на логин, и только после этого заказ будет создан")
    def test_create_order_non_authorized_with_ingredients(self):
        access_token = "invalid_token"
        ingredients = helpers.SampleUserData.get_random_ingredient(2)
        response = api_methods.OrderMethods.create_order(ingredients, access_token)
        assert response.status_code == Responses.UNAUTHORIZED_USER["code"]
        assert response.json()['message'] == Responses.UNAUTHORIZED_USER["message"]

    @allure.title("Получение списка заказов по конкретному юзеру с авторизацией")
    @allure.description("Запрос возвращает код 200 и список заказов пользователя")
    def test_get_orders_by_user_authorized_success(self, create_user_with_deletion):
        user, access_token = create_user_with_deletion
        ingredients = helpers.SampleUserData.get_random_ingredient(2)
        response = api_methods.OrderMethods.create_order(ingredients, access_token)
        order_number = response.json()['order']['number']
        response = api_methods.OrderMethods.get_orders_by_user(access_token)
        assert response.status_code == 200
        assert response.json()["orders"][0]["number"] == order_number
        assert len(response.json()['orders']) == 1

    @allure.title("Получение списка заказов без авторизации")
    @allure.description("Запрос возвращает код 401 и сообщение об ошибке")
    def test_get_orders_by_user_authorized_success(self, create_user_with_deletion):
        user, access_token = create_user_with_deletion
        ingredients = helpers.SampleUserData.get_random_ingredient(2)
        api_methods.OrderMethods.create_order(ingredients, access_token)
        access_token1 = "kfkfkfk"
        response = api_methods.OrderMethods.get_orders_by_user(access_token1)
        assert response.status_code == Responses.UNAUTHORIZED_USER['code']
        assert response.json()["message"] == Responses.UNAUTHORIZED_USER['message']

