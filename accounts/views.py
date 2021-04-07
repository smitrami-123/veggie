from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .models.customUserModel import CustomUser
import uuid
# Create your views here.


def SignUp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = CustomUser.objects.get(email=email), auth_token = auth_token)
            profile_obj.save()
            send_mail_after_signup(auth_token,email)
            #messages.success(request, 'Your Account is created Successfully 😊')
            return redirect('/account/token_sent/')
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


@login_required(login_url='/account/SignIn/')
def SignOut(request):
    logout(request)
    return redirect('/account/SignIn/')

@login_required(login_url='/account/SignIn/')
def userInfo(request):
    return render(request,'accounts/userinfo.html')

def tokenSent(request):
    return  render(request,'accounts/token_sent.html')

def send_mail_after_signup(auth_token, email):
    subject = "VeggieChip verification Mail"
    message = f'Hi, paste this link to verify your account and login http://127.0.0.1:8000/account/verify/{auth_token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)

def verify(request, auth_token) :
    try :
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_verified = True
            messages.success(request, 'Your Account has benn verified')
            return redirect('/account/SignIn/')
        else :
            return redirect('account/error/')
    except Exception as e :
            print(e)

def errorOccured(request) :
    return render(request,'accounts/error.html')