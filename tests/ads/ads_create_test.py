import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    expected_response = {
        'id': 1,
        'author': user.id,
        'category': category.id,
        'description': 'test description',
        'image': None,
        'is_published': False,
        'name': 'test advertisement',
        'price': 1,
    }

    data = {
            "name": "test advertisement",
            "author": user.id,
            "price": 1,
            "description": "test description",
            "is_published": False,
            "category": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.data == expected_response
