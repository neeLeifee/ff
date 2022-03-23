from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    real_name = models.CharField('Имя', max_length=64)
    city = models.CharField('Город', max_length=64)
    birth = models.CharField('Дата рождения', max_length=64)
