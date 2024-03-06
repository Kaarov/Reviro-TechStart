from rest_framework.test import APIClient
import pytest
from faker import Faker

client = APIClient()
fake = Faker()


@pytest.mark.django_db
class TestEstablishment:
    def test_establishment_list(self):
        response = client.get("/establishment/")
        assert response.status_code == 200
