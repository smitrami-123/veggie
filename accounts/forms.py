#
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
#
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
