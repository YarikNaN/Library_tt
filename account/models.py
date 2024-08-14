from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone


# Create your models here.
class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=500)




class BBviser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
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
    taken_date = models.DateTimeField(default=timezone.now)