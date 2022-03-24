from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Из AbstractUser используются так же поля: password, username, email
    klitchka = models.CharField('Кличка', max_length=64, default="")
    city = models.CharField('Город', max_length=64)
    birth = models.CharField('Дата рождения', max_length=64)
    genders = (  # Варианты выбора пола
        ('Мужчина', "Мужчина"),
        ('Женщина', "Женщина"),
        ('Боевой Вертолёт Ка-52 «Аллигатор»', "Боевой Вертолёт Ка-52 «Аллигатор»"),
        ('Булщит', "Булщит"),
    )
    gender = models.CharField('Пол', max_length=100, choices=genders, default='Булщит')
