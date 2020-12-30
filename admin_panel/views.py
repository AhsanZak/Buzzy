from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def admin_panel(request):
    if request.session.has_key('password'):
        return render(request, 'AdminPanel/index.html')
    else:
        return redirect(login)


def login(request):
    if request.session.has_key('password'):
        return redirect(admin_panel)
    else:
        if request.method == 'POST':
            admin = request.POST.get('username')
            password = request.POST.get('password')

            if admin == 'admin' and password == '12345':
                request.session['password'] = password
                return redirect(admin_panel)
            else:
                messages.info(request, "Invalid Credentials")
                return render(request, 'AdminPanel/login.html')

        else:
            return render(request, 'AdminPanel/login.html')


def logout(request):
    request.session.flush()
    return redirect(admin_panel)


def manage_user(request):
    if request.session.has_key('password'):
        details = User.objects.all().order_by('id')
        return render(request, 'AdminPanel/manage_user.html', {'user': details})
    else:
        return redirect(admin_panel)


def add_user(request):
    if request.session.has_key('password'):
        return render(request, 'AdminPanel/register_user.html')
    else:
        return redirect(admin_panel)


def create_user(request):
    if request.session.has_key('password'):
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
                    return render(request, 'AdminPanel/register_user.html')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Taken")
                    return render(request, 'AdminPanel/register_user.html')
                elif User.objects.filter(last_name=last_name).exists():
                    messages.info(request, "Mobile Number Taken")
                    return render(request, 'AdminPanel/register_user.html')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    user.save()
                    return redirect(admin_panel)
            else:
                messages.info(request, "Passwords not Matching")
        else:
            return render(request, 'AdminPanel/register_user.html')
    else:
        return redirect(admin_panel)


def block_user(request):
    pass


def update_user(request):
    pass


def delete_user(request):
    pass


def contents(request):
    if request.session.has_key('password'):
        return render(request, 'AdminPanel/contents.html')
    else:
        return redirect(admin_panel)

def add_contents(request):
    if request.session.has_key('password'):
        return render(request, 'AdminPanel/AddContent.html')
    else:
        return redirect(admin_panel)