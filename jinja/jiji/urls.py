from django.urls import path
from .import views
urlpatterns=[
    path('displaygreen/',views.displaygreen,name='displaygreen')
]