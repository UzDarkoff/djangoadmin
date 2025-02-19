from django.urls import path

from .views import *

urlpatterns = [
    # path('students/', student),
    # path('courses/', course),
    path('course/', index),
]
