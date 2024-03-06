from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from faker import Faker

client = APIClient()
fake = Faker()


@pytest.mark.django_db
class TestAccounts:
    data = {
        "username": fake.user_name(),
        "email": "fake@gmail.com",
        "password": "TestPass123",
        "password2": "TestPass123",
    }

    def test_create_user_no_auth(self):
        response = client.post("/users/register/", self.data)
        assert response.status_code == 200

    def test_login(self, test_user):
        data = {
            "username": test_user.username,
            "password": "TestPass123",
        }
        response = client.post(
            reverse("token_obtain_pair"), data, format="json"
        )
        assert response.status_code == 200
