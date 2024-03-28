from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    iban = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()