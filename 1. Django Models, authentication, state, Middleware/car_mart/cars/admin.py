from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.CarCompany)
admin.site.register(models.Ceo)
admin.site.register(models.CarModel)
admin.site.register(models.FuelType)
