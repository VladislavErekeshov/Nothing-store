from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def index(request):
    return render(request, "main/index.html")

def men(request):
    return render(request, "main/men.html")

def women(request):
    return render(request, "main/women.html")

def fornothing(request):
    return render(request, "main/fornothing.html")

def all(request):
    return render(request, "main/all.html")

def m1(request):
    return render(request, "main/m1.html")

def m2(request):
    return render(request, "main/m2.html")

def m3(request):
    return render(request, "main/m3.html")

def m4(request):
    return render(request, "main/m4.html")

def m5(request):
    return render(request, "main/m5.html")

def m6(request):
    return render(request, "main/m6.html")

def m7(request):
    return render(request, "main/m7.html")

def m8(request):
    return render(request, "main/m8.html")

def m9(request):
    return render(request, "main/m9.html")

def m10(request):
    return render(request, "main/m10.html")

def w1(request):
    return render(request, "main/w1.html")

def w2(request):
    return render(request, "main/w2.html")

def w3(request):
    return render(request, "main/w3.html")

def w4(request):
    return render(request, "main/w4.html")

def w5(request):
    return render(request, "main/w5.html")

def w6(request):
    return render(request, "main/w6.html")

def w7(request):
    return render(request, "main/w7.html")

def w8(request):
    return render(request, "main/w8.html")

def w9(request):
    return render(request, "main/w9.html")

def w10(request):
    return render(request, "main/w10.html")

def buybuybuy(request):
    return render(request, "main/buybuybuy.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered')
            return redirect('main')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = UserLoginForm()
    return render(request, "main/userlogin.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')

def pay(request):
    return render(request, "main/payment.html")
# Create your views here.