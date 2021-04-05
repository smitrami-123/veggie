from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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
    return render(request, 'accounts/login.html')

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
