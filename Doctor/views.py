from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Account


def home(request):
    if request.method == "GET":
        return render(request, 'Doctor/home.html')
    else:
        try:
            if request.POST['password1'] == request.POST['re-password']:
                try:
                    #profile = Profile.objects.all()

                    user = Account.objects.create_user(
                        username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], role=request.POST['role'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except:
                    print(user)
                    return render(request, 'Doctor/home.html', {'error': 'User name already exist. Please choose other username'})
            else:
                return render(request, 'Doctor/home.html', {'error': 'Password did not match'})
        except:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'Doctor/home.html', {'error1': 'User name and password did not match'})
            else:
                login(request, user)
                return redirect('home')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


"""def signupuser(request):
    if request.method == 'GET':
        return render(request,'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error': 'User name already exist. Please choose other username'})
        else:
            return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error': 'Password did not match'})

def currenttodos(request):
    return render(request,'todo/currenttodos.html')"""


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'Doctor/home.html')
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Doctor/home.html', {'error1': 'User name and password did not match'})
        else:
            login(request, user)
            return redirect('home')


"""
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
"""
