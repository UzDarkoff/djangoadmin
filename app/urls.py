from django.urls import path

from .views import student, course

urlpatterns = [
    path('students/', student),
    path('courses/', course),
]
