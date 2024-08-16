from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UpdateProfileForm, UpdateUserForm, UserCreationForm, AuthenticationForm
from .forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth import logout, login
from django.http import JsonResponse
from .utils import is_ajax, classify_face
import base64
from logs.models import Log
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from profiles.models import Profile
from django.views import generic


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
        else:
            form 
    else:
        form = AuthenticationForm()
    return render(request, "logint.html", {"form" : form })






def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form" : form })
    


        

def login_view2(request):
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect('/login')

def logint_view(request):
    return render(request, 'loginT.html', {})


def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        # print(photo)
        decoded_file = base64.b64decode(str_img)
        print(decoded_file)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()

        res = classify_face(x.photo.path)
        if res:
            user_exists = User.objects.filter(username=res).exists()
            if user_exists:
                user = User.objects.get(username=res)
                profile = Profile.objects.get(user=user)
                x.profile = profile
                x.save()

                login(request, user)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    
    



@login_required

def home_view(request):
    profile = Profile.objects.all()
    return render(request, 'bienvenida.html', {"profile": profile})





    
def base(request):
    profile = Profile.objects.all()
    return render(request, 'base.html', {"profile": profile})


@login_required(login_url="/login/")
def Lecturas (request):
    return render (request,'page/index.html', {} )


@login_required(login_url="/login/")
def Sensor1 (request):
    return render (request,'page/sensor1.html', {} )


@login_required(login_url="/login/")
def Sensor2 (request):
    return render (request,'page/sensor2.html', {} )


@login_required(login_url="/login/")
def Sensor3 (request):
    return render (request,'page/sensor3.html', {} )

@login_required(login_url="/login/")
def Sensor4 (request):
    return render (request,'page/sensor4.html', {} )


@login_required(login_url="/login/")
def ceyes(request):
    return render(request, 'bienvenidaceyes.html', {})





@login_required(login_url="/login/")
def Usuario(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')


        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='/')
    else:
        form = PasswordChangeForm(request.user)
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'page/Usuario.html', {
        'form': form, 'user_form': user_form, 'profile_form': profile_form
    })



