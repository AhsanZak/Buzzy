from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from admin_panel.models import ImageDetail
import mimetypes
from wsgiref.util import FileWrapper
from django.core.files.base import ContentFile
import base64
from PIL import Image
from thumbnails.fields import ImageField


def home(request):
    if request.user.is_authenticated:
        return redirect(user_home)
    else:
        user = request.user
        contents = ImageDetail.objects.filter(approval="approved", user__is_staff=True)
        return render(request, 'User/index.html', {'contents': contents})


def user_home(request):
    if request.user.is_authenticated:
        contents = ImageDetail.objects.filter(approval="approved", user__is_staff=True)
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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_number = request.POST['mobile_no']
        email = request.POST['email']
        username = request.POST['username']
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
                                                first_name=first_name, last_name=last_name)
                UserProfile.objects.create(user=user, mobile_number=mobile_number)
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


def view_single(request, image_id):
    content = ImageDetail.objects.filter(id=image_id).first()
    return render(request, 'User/view_single.html', {'content': content})


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
        no_pending = ImageDetail.objects.filter(user=request.user, approval="pending").count()
        return render(request, 'User/creator.html', {'no_pending': no_pending})
    else:
        return redirect(login)


def creator_contents(request):
    if request.user.is_authenticated:
        contents = ImageDetail.objects.filter(user=request.user)
        return render(request, 'User/creator_contents.html', {'contents': contents})
    else:
        return redirect(login)


def delete_content(request, id):
    if request.user.is_authenticated:
        content = ImageDetail.objects.filter(id=id)
        content.delete()
        return redirect(creator_contents)
    else:
        return redirect(login)

def creator_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['wallpaper_name']
            price = request.POST['price']
            category = request.POST['category']
            image = request.FILES['image']
            description = request.POST['description']

            # creating a object
            # creating thumbnail
            # image.save('pythonthumb.png')
            # image.show()
            #
            # format, imgstr = image_data.split(';base64,')
            # ext = format.split('/')[-1]
            # data = ContentFile(base64.b64decode(imgstr), name=name + '.' + ext)

            # image = Image.open(r"C:\Users\ahsan\OneDrive\Desktop\ahsan.jpg")
            # MAX_SIZE = (100, 100)
            # thumbnail = image.thumbnail(MAX_SIZE)

            # image = ImageField(resize_source_to="large")

            ImageDetail.objects.create(name=name, category=category, price=price, image=image, user=request.user,
                                   approval="pending", description=description)

            return redirect(creator_upload)
        else:
            return render(request, 'User/creator_upload.html')
    else:
        return redirect(login)


def creator_settings(request):
    pass


def profile_settings(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        profile = UserProfile.objects.filter(user=user)
        print(profile)
        return render(request, 'User/user_profile.html', {'profile': profile})
    else:
        return redirect(login)


def edit_userProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            user_image = request.FILES.get('user_image')

            if user_image is not None:
                user_profile = UserProfile.objects.filter(user=user)
                if not user_profile:
                    UserProfile.objects.create(user_image=user_image, user=user)
                else:
                    user_profile = UserProfile.objects.get(user=user)
                    user_profile.user_image = user_image
                    user_profile.save()

            return redirect(profile_settings)

        else:
            return redirect(profile_settings)
    else:
        return redirect(login)


def download_image(request, image_id):
    image = ImageDetail.objects.get(id=image_id)
    image_url = image.image_url()

    wrapper = FileWrapper(open(image_url, 'rb'))

    content_type = mimetypes.guess_type(image_url)[0]
    response = HttpResponse(wrapper, mimetype=content_type)
    response['Content-Disposition'] = "attachment; filename=%s" % image_url
    return response
