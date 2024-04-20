from django.db import models

class quiz(models.Model):
    id = models.CharField('id', max_length=50, primary_key=True, unique=True, name='id')
    text = models.CharField('text', max_length=200, name='text')
    yes = models.CharField('yes', max_length=50, name='yes')
    no = models.CharField('no', max_length=50, name='no')
