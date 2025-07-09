from django.urls import path
from . import views
urlpatterns = [
   
   path('mca/',views.mca, name='mca'),
	]