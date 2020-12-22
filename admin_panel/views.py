from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def admin_panel(request):
    if request.session.has_key('password'):
        return render(request, 'AdminPanel/index.html')
    else:
        return redirect(login)


