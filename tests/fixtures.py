import pytest
# from rest_framework.test import APIClient


@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = "username"
    password = "password"

    django_user_model.objects.create_user(username=username, password=password)
    response = client.post(
        "/user/token/",
        {
            "username": username,
            "password": password
        },
        format='json')

    return response.data["access"]


# @pytest.fixture()
# def client() -> APIClient:
#     return APIClient()
#
# # тогда в тестах
# def test_foo(client, user):
#     client.forse_login(user)
#     response = client.post(...)
