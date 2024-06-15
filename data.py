class URLs:
    BASE_URL = ' https://stellarburgers.nomoreparties.site'
    CREATE_USER_ENDPOINT = '/api/auth/register'
    USER_ENDPOINT = '/api/auth/user'
    LOGIN_USER_ENDPOINT = '/api/auth/login'
    ORDERS_ENDPOINT = '/api/orders'
    INGREDIENTS_ENDPOINT = '/api/ingredients'
    INGREDIENTS_URL = f'{BASE_URL}{INGREDIENTS_ENDPOINT}'
    REGISTER_URL = f'{BASE_URL}{CREATE_USER_ENDPOINT}'
    USER_URL= f'{BASE_URL}{USER_ENDPOINT}'
    LOGIN_URL = f'{BASE_URL}{LOGIN_USER_ENDPOINT}'
    ORDERS_URL = f'{BASE_URL}{ORDERS_ENDPOINT}'


class Responses:
    NO_INGREDIENTS_PROVIDED = {"code": 400, "message": "Ingredient ids must be provided"}
    UNKNOWN_INGREDIENT_ID = {"code": 500, "message": 'One or more ids provided are incorrect'}
    UNAUTHORIZED_USER = {"code": 401, "message": 'You should be authorised'}
    INCORRECT_PASSWORD = {"code": 401, "message": 'email or password are incorrect'}
    USER_ALREADY_EXISTS = {"code": 403, "message": 'User already exists'}
    NO_REQUIRED_FIELDS_PROVIDED = {"code": 403, "message": 'Email, password and name are required fields'}
