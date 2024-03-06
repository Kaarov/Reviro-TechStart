from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model"""

    email = models.EmailField("Email Address", unique=True, blank=True, null=True)
    username = models.CharField(verbose_name="Username", max_length=100, unique=True, null=True, blank=True)
    avatar = models.ImageField("Avatar", upload_to='users-avatar/', blank=True, null=True)
    birth_date = models.DateField("Birth Day", null=True, blank=True)

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return "{username}".format(username=self.get_username())


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    establishment = models.CharField("Establishment Name", max_length=255)
    location = models.CharField("Location", max_length=255)
    description = models.TextField("Description")
    phone_number = models.CharField("Phone Number", max_length=20)
    avatar = models.ImageField(upload_to='partners_avatars/', blank=True, null=True)

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return f'{self.user.username} - {self.establishment}'
