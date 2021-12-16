from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'main.html')

# def register(request):
#     return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        errors=User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(rounds = 10)).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash,
        )
        request.session['user_id'] = new_user.id
        return redirect('/tables')
    return redirect('/')


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