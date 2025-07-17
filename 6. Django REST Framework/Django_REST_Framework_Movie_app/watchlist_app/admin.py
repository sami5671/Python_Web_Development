from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.MovieList)
admin.site.register(models.Reviews)
