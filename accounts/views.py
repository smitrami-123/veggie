from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def SignUp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return  render(request, 'accounts/signup.html', context)

def SignIn(request):
    return render(request,'accounts/login.html')