# accounts/views.py
from .models import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def home(request):
    UD = CustomUser.objects.all()
    return render(request,'home.html',{'UD':UD})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         user = request.POST['user']
#         if request.user.is_superuser:
#             UD = CustomUser.objects.all()
#             return render(request,'home.html',{'UD':UD})
#     return render(request,'login.html')