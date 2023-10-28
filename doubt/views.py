import re
from django.shortcuts import render, HttpResponse, redirect
from doubt.models import doubt, Answer
from django.contrib import messages
from django.contrib.auth.models import User


def doubthome(request):
    allPosts = doubt.objects.all()
    context = {'allPosts': allPosts}
    return HttpResponse("Coming soon....")
