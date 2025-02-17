from django.shortcuts import render
from .models import *
def student(request):
    students=Student.objects.all()

    context={
        "student":students,
        "title":"Students"
    }
    return render(request,'Students/student.html',context=context)

def course(request):
    courses=Course.objects.all()

    context={
        "course":courses,
        "title":"Courses"
    }
    return render(request,'Courses/course.html',context=context)


