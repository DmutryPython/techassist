from django.db import models
from datetime import datetime


class user(models.Model):
    name = models.CharField('name', max_length=50)
    surname = models.CharField('surname', max_length=50)
    login = models.CharField('login', unique=True, max_length=200, primary_key=True)
    password = models.CharField('password', max_length=200)
    appel = models.TextField('appel', default=' ')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
