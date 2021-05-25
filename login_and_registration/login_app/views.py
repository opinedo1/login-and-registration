from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    return redirect('/')
    
def login(request):
    if request.method == "GET":
        return redirect('/')
    return redirect('/')

def logout(request):
    return redirect('/')

def success(request):
    return redirect('/')
