from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'receipt'
urlpatterns = [
    path('create/', views.CreateReceiptRequest.as_view()),    
    re_path(r'^detail/(?P<task_id>[\w-]+)/$', views.GetStateOfTaskById.as_view()),    
]
