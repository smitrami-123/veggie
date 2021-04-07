from django.db import models
from   .customUserModel import CustomUser, CustomUserManager


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
