from django.contrib import admin

from .models import Category, Course, Enrollment, Lesson, Material, QuestionAnswer

# Register your models here.
admin.site.register([Category, Course, Enrollment, Lesson, Material, QuestionAnswer])
