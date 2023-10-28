from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
import markdown2


def home(request):
    return render(request, 'home/home.html')


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        address = request.POST['address']
        phone_no = request.POST['phonenumber']
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # Check for erroneous input
        if len(username) >= 10:
            messages.error(
                request, "Your user name must be under 10 characters")
            return redirect("main")

        if not username.isalnum():
            messages.error(
                request, "Username should only contain letters and numbers")
            return redirect("main")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("main")

        if len(phone_no) != 10:
            messages.error(request, "Please enter correct phone number")
            return redirect("main")

        # Create the user
        try:
            user = User.objects.create_user(
                username=username, email=email, password=pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()

            messages.success(request, "Welcome to VedaQuest")
            return redirect("main")

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect("main")

    return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")


def generate_slug(title):
    slug = re.sub(r'\s+', '+', title)
    return slug


def doubt(request):
    return HttpResponse("Coming soon...")


def task(request):
    return HttpResponse("Coming soon...")
