from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from admin_panel.models import ImageDetail
import mimetypes
from wsgiref.util import FileWrapper


def home(request):
    if request.user.is_authenticated:
        return redirect(user_home)
    else:
        contents = ImageDetail.objects.all()
        return render(request, 'User/index.html', {'contents': contents})


def user_home(request):
    if request.user.is_authenticated:
        contents = ImageDetail.objects.all()
        user = request.user
        return render(request, 'User/home.html', {'contents': contents, 'user': user})
    else:
        return redirect(home)


def about(request):
    return render(request, 'User/about.html')


def contact(request):
    return render(request, 'User/contact.html')


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
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(home)
    else:
        return redirect(home)


def single(request, image_id):
    content = ImageDetail.objects.filter(id=image_id).first()
    print(content.image)
    return render(request, 'User/single.html', {'content': content})


def activate_creator(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        if user.is_staff == False:
            user.is_staff = True
            user.save()
        return redirect(user_home)
    else:
        return redirect(login)


def Deactivate_creator(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        if user.is_staff == True:
            user.is_staff = False
            user.save()
        return redirect(user_home)
    else:
        return redirect(login)


def creator(request):
    if request.user.is_authenticated:
        return render(request, 'User/creator.html')
    else:
        return redirect(login)


def creator_contents(request):
    if request.user.is_authenticated:
        return render(request, 'User/creator_contents.html')
    else:
        return redirect(login)


def creator_upload(request):
    if request.user.is_authenticated:
        return render(request, 'User/creator_upload.html')
    else:
        return redirect(login)


def creator_settings(request):
    pass


def profile_settings(request):
    pass


def download_image(request, image_id):
    image = ImageDetail.objects.get(id=image_id)
    image_url = image.image_url()

    wrapper = FileWrapper(open(image_url, 'rb'))

    content_type = mimetypes.guess_type(image_url)[0]
    response = HttpResponse(wrapper, mimetype=content_type)
    response['Content-Disposition'] = "attachment; filename=%s" % image_url
    return response
