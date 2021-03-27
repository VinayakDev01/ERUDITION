from django.views import generic
from .models import userprofile
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserProfileForm , UserUpdateForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'movie/index.html')



#-------------------Launguages---------------------

def python_file(request):
    return render(request, 'movie/py.html')

def c_file(request):
    return render(request, 'movie/c.html')

def cpp_file(request):
    return render(request, 'movie/cpp.html')

def java_file(request):
    return render(request, 'movie/java.html')

def ds_file(request):
    return render(request, 'movie/ds.html')

def php_file(request):
    return render(request, 'movie/php.html')





#----------------Interview Portal----------------

def python_questions(request):
    return render(request, 'movie/interview/pyinterview.html')

def c_questions(request):
    return render(request, 'movie/interview/cinterview.html')

def cpp_questions(request):
    return render(request, 'movie/interview/cppinterview.html')

def java_questions(request):
    return render(request, 'movie/interview/javainterview.html')

def ds_questions(request):
    return render(request, 'movie/interview/dsinterview.html')

def php_questions(request):
    return render(request, 'movie/interview/phpinterview.html')

def html_questions(request):
    return render(request, 'movie/interview/htmlinterview.html')

def css_questions(request):
    return render(request, 'movie/interview/cssinterview.html')

def js_questions(request):
    return render(request, 'movie/interview/jsinterview.html')

def django_questions(request):
    return render(request, 'movie/interview/djangointerview.html')

def dbms_questions(request):
    return render(request, 'movie/interview/dbmsinterview.html')






#------------------user register and login----------------------------------------------


def Signup(request):
    form = UserForm(request.POST or None)
    profile_form = UserProfileForm(request.POST, request.FILES)
    
    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        profile = profile_form.save(commit= False)
        profile.user = user

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        profile.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'movie/index.html')
    context = {
        "form": form,
        "profile_form":profile_form,
    }
    return render(request, 'movie/signup.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'movie/index.html')
            else:
                return render(request, 'movie/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'movie/login.html', {'error_message': 'Invalid login'})
    return render(request, 'movie/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'movie/login.html' , context)


@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'movie/profile.html', {'user': user})


def edit_names(request):
    Error =""
    if request.method == "POST":
        # line 324,325,326,327,328 for checking your password is write or wrong.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:

                form = UserUpdateForm(data=request.POST, instance=request.user)
                profile_form = UserProfileForm(request.POST, instance= request.user.userprofile)
                if form.is_valid() and profile_form.is_valid():
                    user = form.save()
                    profile = profile_form.save(commit=False)
                    profile.user = user
                    if 'profile_photo' in request.FILES:
                        profile.profile_photo = request.FILES['profile_photo']
                    profile.save()
                    url = reverse('movie:index')

                    return HttpResponseRedirect(url)
                else:
                    error_message =""
                    print(form.errors, profile_form.errors)
            else:
                Error ="User is Not Active"
        else:
            Error = "Wrong Password! For Update Your information you have to enter right password."

    form = UserUpdateForm(instance=request.user)
    profile_form = UserProfileForm( instance= request.user.userprofile)

    return render(request, "movie/update_user.html",{"form":form, "profile_form":profile_form,"Error":Error})

def PasswordChangeComplete(request):
    return render(request, 'movie/commons/change_password_complete.html', {})



#-------------------Launguages---------------------

def report(request):
    return render(request, 'movie/report.html')

def privacy(request):
    return render(request, 'movie/privacy.html')

def term(request):
    return render(request, 'movie/term.html')

def about(request):
    return render(request, 'movie/about.html')

def contact(request):
    return render(request, 'movie/contact.html')

def copyright(request):
    return render(request, 'movie/copyright.html')

