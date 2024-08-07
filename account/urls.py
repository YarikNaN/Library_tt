import django.contrib.auth.views
from django.urls import path

import reader.views
from reader.views import BookListView, MyBooksListView
from . import views

urlpatterns = [
    # post views
     path('login', views.user_login, name='login'),
     path('register', views.register, name='register'),
     path("dashboard", BookListView.as_view(), name='books'),
     path("mybooks", MyBooksListView.as_view(), name='mybooks'),





    # path('login', django.contrib.auth.views.login, name='login'),
    # path('logout', django.contrib.auth.views.logout, name='logout'),



]