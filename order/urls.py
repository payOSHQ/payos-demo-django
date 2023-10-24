
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import *
# 

urlpatterns = [
    path('create', OrderCreate.as_view()),
    path('<int:pk>', OrderManage.as_view()),
]
