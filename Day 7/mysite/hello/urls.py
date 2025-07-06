from django.db import models

# Create your models here.
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('demo/', views.demo, name='demo'),

]
