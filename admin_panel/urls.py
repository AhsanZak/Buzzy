
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name="admin_panel"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="admin_logout"),

    path('manage-user', views.manage_user, name="manage-user"),
    path('add-user', views.add_user, name="add_user"),
    path('create-user', views.create_user, name="create_user"),
]
