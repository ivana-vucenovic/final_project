from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    nurses = Nurse.objects.all()
    context ={
        'nurses': nurses
    }
    return render(request, 'main.html', context)

def register(request):
    return render(request, 'register.html')

def register_user(request):
    if request.method == 'POST':
        errors=User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(rounds = 10)).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            phone_number=request.POST['telNo'],
            email=request.POST['email'],
            password=pw_hash,
        )
        request.session['user_id'] = new_user.id
        return redirect('/login')
    return redirect('/register')

def login(request):
    return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/send')
    return redirect('/')

def send(request):
    return render(request, 'send.html')
    
def contact(request):
    pass

def aboutUs(request):
    pass

def requestQuote(request):
    pass
def nurses(request):
    nurses = Nurse.objects.all()
    context ={
        'nurses': nurses
    }
    return render(request, 'nurses.html', context)

def delete(request, nurse_id):
    to_delete = Nurse.objects.get(id=nurse_id)
    to_delete.delete()
    return redirect('/nurses')

def add_a_nurse(request):
    return render(request, 'add_a_nurse.html')

def create(request):
    errors = Nurse.objects.nurse_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/add_a_nurse')
    else:
        user = User.objects.get(id=request.session["user_id"])  
        new_nurse = Nurse.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            tel = request.POST['tel'],
            email = request.POST['email'],
        )
        print(new_nurse.id)
    return redirect('/nurses')

