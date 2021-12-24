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
    path('add_a_nurse', views.add_a_nurse),
    path('create', views.create),
    path('nurse/<int:nurse_id>/delete', views.delete),
    path('contact', views.contact),
    path('aboutUs', views.aboutUs),
    path('requestQuote', views.requestQuote),
]
