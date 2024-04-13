from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

def index(request):
    
    return render(request, "index.html")


def registeruser(request):
    if request.method == 'POST':
        forms = Register(request.POST)
        if forms.is_valid():
            
            
            user = forms.save()
            
            login(request ,user)
            return redirect('index')
        
    else:
        forms = Register()
    return render(request , 'login/register.html', {'forms':forms})


def Loginuser(request):
    if request.method=='POST':
        forms = AuthenticationForm(request, request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request,user)
            return redirect('index')
    else:
        forms = AuthenticationForm()
    return render(request, "login/login.html", {"forms":forms})

def salir(request):
    logout(request)
    
    return redirect("index")