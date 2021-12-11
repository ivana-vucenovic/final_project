from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('register', views.register),
    path('login', views.login),
    path('send', views.send),
    path('contact', views.contact),
    path('aboutUs', views.aboutUs),
    path('requestQuote', views.requestQuote),
]
