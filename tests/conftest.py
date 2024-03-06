from pytest_factoryboy import register
from tests import factories
import pytest

register(factories.ProductFactory)
register(factories.EstablishmentFactory)
register(factories.UserFactory)


@pytest.fixture()
def test_product(db, product_factory):
    product = product_factory.create()
    product.save()
    return product


@pytest.fixture()
def test_establishment(db, establishment_factory):
    establishment = establishment_factory.create()
    establishment.save()
    return establishment


@pytest.fixture()
def test_user(db, user_factory):
    user = user_factory.create()
    user.set_password("TestPass123")
    user.save()
    return user


@pytest.fixture()
def test_partner_user(db, user_factory):
    user = user_factory.create()
    user.set_password("TestPass123")
    user.save()
    return user
