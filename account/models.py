from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    email = models.EmailField(null = True, blank = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # forgot_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username

class ForgetPasswordOTP(models.Model):
    otp = models.CharField(max_length = 4)
    created_on = models.DateTimeField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username
