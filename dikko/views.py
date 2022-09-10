from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Registeration
from .forms import RegisterationForm, CreateUserForm
from .decorators import unauthenticated_user

def home(request):
    return render(request, 'index.html')

@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('login')
        else:
            return redirect('signup')

    context = {
        "form":form,
    }
    return render(request, 'signup.html', context )

@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)     
            return redirect('registeration')
        else:
            messages.info(request, 'username or password is not correct')  

    return render(request, 'login.html')


def registeration(request):
    my_user = request.user
    user_registeration = Registeration.objects.filter(user = my_user).first()
    if user_registeration:
        return redirect('home')
    else:
        form = RegisterationForm(initial={
            'user':my_user
        })
        if request.method == 'POST':
            form = RegisterationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')

        context = {
            'form':form
        }

    return render(request, 'registeration.html', context)

def success(request):
    return render(request, 'success.html')

def Logout(request):
    logout(request)
    return redirect('home')