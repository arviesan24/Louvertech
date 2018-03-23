from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import AccountRegistrationForm, AccountLoginForm
from django.contrib import messages

# Create your views here.

def accounts_signup(request):
    # next = request.GET.get("next")
    form = AccountRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.is_active = False
        user.save()
        # login(request, user)
        # if next:
        #     return redirect(next)
        messages.info(request, 'Your registration is complete. Please wait for the admin approval.')
        # return redirect("/")

    context = {
        "form": form,
    }

    return render(request, "forms/registration_form.html", context)

def accounts_login(request):
    next = request.GET.get("next")
    form = AccountLoginForm(request.POST or None)

    if form.is_valid():


        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form
    }

    return render(request, "forms/login_form.html", context)


def accounts_logout(request):
    logout(request)
    # if not AnonymousUser:
    #     return redirect("/accounts/login/")
    messages.success(request, 'You have been logged out successfully.')

    return redirect("/accounts/login/")

#TODO: fix signals to avoid is_active getting disabled all the time, it should only work on user registration
#TODO: create 404 page