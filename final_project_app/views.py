from django.shortcuts import render, redirect
# from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'main.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def send(request):
    return render(request, 'send.html')
    
def contact(request):
    pass

def aboutUs(request):
    pass

def requestQuote(request):
    pass
def nurses(request):
    return render(request, 'nurses.html')