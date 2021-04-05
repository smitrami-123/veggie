from django.contrib import admin
from django.urls import path, include
from .views import SignIn,SignUp,SignOut,userInfo

urlpatterns = [
   path('SignIn/', SignIn),
   path('SignUp/', SignUp),
   path('userinfo/',userInfo),
   path('SignOut/', SignOut,name = 'logout'),

]
