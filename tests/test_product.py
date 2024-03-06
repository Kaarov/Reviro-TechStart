from rest_framework.test import APIClient
import pytest
from faker import Faker

client = APIClient()
fake = Faker()


@pytest.mark.django_db
class TestProduct:
    def test_product_list(self):
        response = client.get("/product/")
        assert response.status_code == 200
