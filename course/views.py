from django.shortcuts import render, HttpResponse
from course.models import Course, Quiz, Lecture, Test
# Create your views here.


def course(request):
    return HttpResponse("Courses here")


def coursehome(request):
    return render(request, 'course/main.html')
