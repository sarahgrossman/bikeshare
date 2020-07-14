from django.db import models
from users.models import User

# Create your models here.


class Bicycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=64)