from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('register', views.register),
    path('register_user', views.register_user),
    path('login', views.login),
    path('login_user', views.login_user),
    path('send', views.send),
    path('nurses', views.nurses),
    path('contact', views.contact),
    path('aboutUs', views.aboutUs),
    path('requestQuote', views.requestQuote),
]
