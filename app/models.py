from django.db import models
from django.db.models import ForeignKey


class Student(models.Model):
    full_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name="STUDENT"
        verbose_name_plural="STUDENTS"
        ordering=['-pk']

class Course(models.Model):
    title=models.CharField(max_length=50)
    describtion=models.TextField(blank=True)
    start_time=models.TimeField()
    end_time=models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "COURSE"
        verbose_name_plural = "COURSES"
        ordering = ['-pk']

# class Categories(models.Model):
#     title=models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title
#
# class News(models.Model):
#     title = models.CharField(max_length=50)
#     context = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category=ForeignKey(Categories, on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     is_bool = models.BooleanField(default=True)
#
#
#     def __str__(self):
#         return self.title





