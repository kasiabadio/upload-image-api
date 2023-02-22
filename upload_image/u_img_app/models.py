from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, verbose_name="nazwa użytkownika", default="null")
    email = email = models.EmailField(verbose_name="email", max_length=60) 
    name = models.CharField(max_length=50, verbose_name="imię", default="null")
    surname = models.CharField(max_length=50, default="null")

    BASIC = 'B'
    PREMIUM = 'PR'
    ENTERPRISE = 'E'
    ACCOUNT_TIERS = [
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        (ENTERPRISE, 'Enterprise'),
    ]

    account_tiers = models.CharField(max_length=2, choices=ACCOUNT_TIERS, default=BASIC)
    USERNAME_FIELD = 'username'


class Image(models.Model):
    id_image = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    url = models.URLField(max_length=200)
    image = models.ImageField(null=True)

    PNG = 'P'
    JPG = 'J'
    FORMAT_CHOICES = [
        (PNG, 'PNG'), 
        (JPG, 'JPG')
    ]
    format = models.CharField(max_length=1, choices=FORMAT_CHOICES, default=JPG)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    