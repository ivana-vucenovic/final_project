from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first_name']) < 2:
            errors ['first_name'] = "First Name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors ['email'] = "That email is already in use"
        if len(postData['password']) < 8:
            errors ['password'] = "Password should be at least 8 characters long"
        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Password and PW_Confirm did not match!"
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors ['email'] = "Email required"
        if len(postData['password']) < 8:
            errors ['password'] = "Password should be at least 8 characters long"
        if bcrypt.checkpw(postData['password'].encode(),existing_user[0].password.encode()) != True:
            errors['password'] = 'Email and password do not match'
        return errors

class NurseManager(models.Manager):
    def nurse_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first_name']) < 2:
            errors ['first_name'] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors ['last_name'] = "Last Name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors ['email'] = "That email is already in use"
        return errors

class PSWManager(models.Manager):
    def psw_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first_name']) < 2:
            errors ['first_name'] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors ['last_name'] = "Last Name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors ['email'] = "That email is already in use"
        return errors


class User(models.Model):
    first_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    phone_number = models.CharField(max_length=255, null=True)
    password=models.CharField(max_length=12)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Nurse(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    tel= models.CharField(max_length=255, null=True)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    this_nurse = models.ForeignKey(User, related_name='nurses', on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=NurseManager()

class PSW(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    this_PSW = models.ForeignKey(User, related_name='psws', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=PSWManager()


