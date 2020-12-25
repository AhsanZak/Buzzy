from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect(user_home)
    else:
        return render(request, 'User/index.html')

def user_home(request):
    if request.User.is_authenticated:
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
        name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        dic = {'name': name, 'email': email, 'username': username}

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return render(request, 'User/signup.html', dic)
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=name)
                user.save()
                print("User created")
                return redirect(login)
        else:
            messages.info(request, "Passwords Not Matching")
            return render(request, 'User/signup.html', dic)

    else:
        return render(request, 'User/signup.html')


def logout(request):
    pass
