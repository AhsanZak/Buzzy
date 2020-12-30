
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
    path('update-user/<int:id>', views.update_user, name="update_user"),
    path('block-user/<int:id>', views.block_user, name="block_user"),
    path('delete-user/<int:id>', views.delete_user, name="delete_user"),

    path('contents', views.contents, name="contents"),
    path('add-contents', views.add_contents, name="add_contents"),
]
