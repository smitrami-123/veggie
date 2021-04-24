from accounts.models.customUserModel import CustomUser
from django.db import models
class Customer(models.Model) :
    user = models.OneToOneField(CustomUser,null = True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name