from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import LoginForm
from django.contrib import messages




def home_view(request):
    if request.user.is_authenticated:
        return redirect('track')
    else:
        return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('track')
        
    else:
        form = CustomUserCreationForm()
    return render(request,  'USERS/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('track')
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Invalid email or password")
                
    else:
        form  = LoginForm()
    return render(request,  'USERS/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
            