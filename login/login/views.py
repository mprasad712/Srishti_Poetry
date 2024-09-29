from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

def signin(request):
    return render(request, "login/login.html")

def signup(request):
    return render(request, 'login/signup.html')

def forgot_password(request):
    return HttpResponse("Forgot Password")

def homepage(request):
    return render(request, 'homepage/index.html')

def poems(request):
    return render(request, 'homepage/poems.html')

def register(request):
    if request.method == 'POST':
        # Extract form data
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('pass')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already taken!"
            return render(request, 'login/signup.html', {'error_message': error_message})

        if User.objects.filter(email=email).exists():
            error_message = "Email already registered!"
            return render(request, 'login/signup.html', {'error_message': error_message})

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = full_name
        user.save()

        # Automatically log in the user after registration
        auth_login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('home')  # Redirect to home or any other page you wish after registration

    return render(request, 'login/signup.html')  # Ensure correct template path

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to a home or dashboard page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login/login.html')  # Correct the template path for unsuccessful login
