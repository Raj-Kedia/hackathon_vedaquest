from django.urls import path
from doubt import views

urlpatterns = [
    path("", views.doubthome, name='doubthome'),
]
