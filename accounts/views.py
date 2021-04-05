from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def SignUp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account is created Successfully 😊')
            return redirect('/account/SignIn/')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def SignIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email, password=password)
        if user is not None :
            login(request,user)
            return redirect('/home/')
        else:
            messages.info(request, 'Credentials are incorrect')
    return render(request, 'accounts/login.html')

def SignOut(request):
    logout(request)
    return redirect('/account/SignIn/')

login_required(login_url='/account/SignIn/')
def userInfo(request):
    return render(request,'accounts/userinfo.html')

# def register(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         # form.username = form.email
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request,'accounts/Register.html',context)
#
# def Login(request):
#
#     return render(request, 'accounts/goin.html')
