from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomeUser
from authentication.forms import CustomerSignupForm

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})

def logout_user(request):
    
    logout(request)
    return redirect('login')

def signup(request):
    context = {}
    
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context["errors"] = form.errors
    form = CustomerSignupForm()
    context["form"] = form

    return render(request, 'authentication/signup.html', context=context)
