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
