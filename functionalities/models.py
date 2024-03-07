from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Functionalities(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez d'autres champs si nécessaire pour votre application