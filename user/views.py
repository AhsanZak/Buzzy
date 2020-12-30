from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def common_home(request):
    return render(request, 'User/index.html')

def about(request):
    return render(request, 'User/about.html')

def contact(request):
    return render(request, 'User/contact.html')

def home(request):
    if request.user.is_authenticated:
        return redirect(user_home)
    else:
        return render(request, 'User/about.html')


def user_home(request):
    if request.user.is_authenticated:
        return render(request, 'User/UserHome.html')
    else:
        return redirect(login)


def login(request):
    if request.user.is_authenticated:
        return redirect(user_home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(user_home)
        else:
            messages.info(request, "Invalid credentials")
            return redirect(login)
    else:
        return render(request, 'User/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['full_name']
        email = request.POST['email']
        username = request.POST['username']
        last_name = request.POST['mobileNo']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return render(request, 'User/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return render(request, 'User/signup.html')
            elif User.objects.filter(last_name=last_name).exists():
                messages.info(request, "Mobile Number Taken")
                return render(request, 'User/signup.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords Not Matching")
            return render(request, 'User/signup.html')

    else:
        return render(request, 'User/signup.html')


def logout(request):
    pass
