from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField( unique=True)
    first_name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, null=True, verbose_name='Фамилия')
    username = models.CharField(max_length=20, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=200, verbose_name='Пароль')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username