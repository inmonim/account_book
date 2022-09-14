from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout

# Create your views here.
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('main:index')
    
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form.as_p,
    }
    return render(request, 'users/form.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('main:index')
    
    else:
        form = AuthenticationForm()
    
    context ={
        'form':form.as_p()
    }

    return render(request, 'users/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('users:login')