from django.urls import path
from course import views

urlpatterns = [
    path("", views.coursehome, name='coursehome'),
    path("course", views.course, name='course'),
]
