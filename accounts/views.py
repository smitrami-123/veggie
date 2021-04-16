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
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
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

@unauthenticated_user
def SignIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email, password=password)

        if user is not None :
            user_obj = CustomUser.objects.get(email=email)
            profile_obj = Profile.objects.get(user=user_obj)
            if not profile_obj.is_verified :
                messages.success(request, 'Your Account is not yet verified.')
                messages.success(request, 'Please Check your mail box')
                return redirect('/account/SignIn/')
            login(request,user)
            request.session['user_id'] = user_obj.id
            request.session['user_email'] = user_obj.email
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
    return render(request, 'accounts/userinfo.html')


def tokenSent(request):
    return  render(request, 'accounts/token_sent.html')


def send_mail_after_signup(auth_token, email):
    subject = "VeggieChip verification Mail"
    message = f'Hi, paste this link to verify your account and login http://127.0.0.1:8000/account/verify/{auth_token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.get(auth_token=auth_token)
        if profile_obj:
            if profile_obj.is_verified :
                messages.success(request, 'Your Account has been already verified')
                return redirect('/account/SignIn/')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your Account has been verified')
            return redirect('/account/SignIn/')
        else :
            return redirect('account/error/')
    except Exception as e :
            print(e)

def errorOccured(request) :
    return render(request,'accounts/error.html')