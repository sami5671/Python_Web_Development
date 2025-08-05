from django.db import models

from lms_backend.models.base_model import BaseModel
from users.models import User


# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner = models.ImageField(upload_to="course_banners/")
    price = models.FloatField()
    duration = models.FloatField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"role": "teacher"}
    )

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to="lesson_videos")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Material(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_type = models.CharField(max_length=100)
    file = models.FileField(upload_to="materials/")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)


class QuestionAnswer(BaseModel):
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.user_id.username} --> {self.lesson_id.title} --> {self.description}"
        )


class Enrollment(BaseModel):
    price = models.FloatField()
    progress = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    is_certificate_ready = models.BooleanField(default=False)
    total_mark = models.FloatField(default=0)
    student_id = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"role": "student"}
    )
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"
