from django.contrib import admin
from django.urls import path
from .views import SignIn,SignUp

urlpatterns = [
    path('SignIn/', SignIn),
    path('SignUp/', SignUp)
]
