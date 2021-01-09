from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user-home', views.user_home, name="user_home"),
    path('login', views.login, name="login"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),

    path('activate-creator/<int:user_id>', views.activate_creator, name="activate_creator"),
    path('deactivate-creator/<int:user_id>', views.Deactivate_creator, name="deactivate_creator"),

    path('creator', views.creator, name="creator"),
    path('creator-contents', views.creator_contents, name="creator_contents"),
    path('creator-upload', views.creator_upload, name="creator_upload"),

    path('profile-settings', views.profile_settings, name="profile_settings"),
    path('creator-settings', views.creator_settings, name="creator_settings"),

    path('single/<int:image_id>', views.single, name="single"),
    path('download-image/<int:image_id>', views.download_image, name="download_image")
]
