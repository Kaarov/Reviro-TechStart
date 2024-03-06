import factory
from product.models import Product
from establishment.models import Establishment
from users.models import User

from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = fake.user_name()
    is_staff = True
    password = "TestPass123"
    is_superuser = True


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = fake.sentence()
    description = fake.text()
    price = fake.random_int(min=1, max=100)
    quantity = fake.random_int(min=1, max=100)


class EstablishmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Establishment

    name = fake.sentence()
    description = fake.text()
    location = fake.text(max_nb_chars=100)
    opening_hours = fake.random_int(min=1, max=100)
