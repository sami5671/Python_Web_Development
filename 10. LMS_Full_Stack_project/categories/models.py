from django.db import models

from core.models.base_model import BaseModel


# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=255, unique=True)
