from django.shortcuts import render

# Create your views here.

def SignUp(request):

    return  render(request,'accounts/signup.html')

def SignIn(request):
    return render(request,'accounts/login.html')