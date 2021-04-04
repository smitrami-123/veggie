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
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
