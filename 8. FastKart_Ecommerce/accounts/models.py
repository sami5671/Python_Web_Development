from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    address_line_1 = models.CharField(null=True, blank=True, max_length=100)
    address_line_2 = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=20)
    postcode = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    mobile = models.CharField(null=True, blank=True, max_length=15)

    profile_picture = models.ImageField(null=True, blank=True, upload_to="user_profile")

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"
