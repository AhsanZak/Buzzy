
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel),
    path('login', views.login),
]
