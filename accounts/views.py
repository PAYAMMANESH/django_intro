from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd["username"], cd["email"], cd["password"])
            user.first_name = cd["firstname"]
            user.last_name = cd["lastname"]
            user.save()
            return redirect("Home")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", context={"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                return redirect("Home")
            else:
                messages.error(request, "sth went wrong", "danger")

    else:
        form = UserLoginForm()
    return render(request, "Login.html", context={"form": form})

def user_logout(request):
    logout(request)
    return redirect('Home')