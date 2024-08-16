import django.contrib.auth.views
from django.urls import path

import reader.views
from bible_superviser.views import UsersListView
from reader.views import BookListView, MyBooksListView
from . import views
from .views import custom_logout

urlpatterns = [
    # post views
     path('login', views.user_login, name='login'),
     path('logout', custom_logout, name='logout'),
     path('register', views.register, name='register'),
     path('svregister', views.svregister, name='svregister'),
     path("dashboard", BookListView.as_view(), name='books'),
     path("mybooks", MyBooksListView.as_view(), name='mybooks'),
     path("debt", UsersListView.as_view(), name='debt'),
     path('logout', django.contrib.auth.logout, name='logout'),





    # path('login', django.contrib.auth.views.login, name='login'),
    # path('logout', django.contrib.auth.views.logout, name='logout'),



]