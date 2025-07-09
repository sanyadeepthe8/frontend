from django.urls import path
from . import views
urlpatterns = [
   
   path('mba/',views.mba, name='mba'),
	]