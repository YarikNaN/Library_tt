from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Reader(AbstractUser):
    username = models.CharField(max_length=355, unique=True)
    password = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=500)



class BBviser(models.Model):
    username = models.CharField(max_length=355)
    password = models.CharField(max_length=500)
    tab_id = models.CharField(max_length=100)


class Books(models.Model):
    title = models.CharField(max_length=355)
    author = models.CharField(max_length=355)
    genre = models.CharField(max_length=255)

    class Meta:
        ordering = ['title']


class TakenBooks(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    