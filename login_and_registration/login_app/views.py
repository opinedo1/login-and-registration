from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        user = User.objects.register(request.POST)
        return redirect('/')
    
def login(request):
    if request.method == "GET":
        return redirect('/')
    return redirect('/')

def logout(request):
    return redirect('/')

def success(request):
    return redirect('/')
