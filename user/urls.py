from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.UserListCreate.as_view()),
]
