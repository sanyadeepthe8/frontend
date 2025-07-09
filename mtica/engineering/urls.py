from django.urls import path
from . import views
urlpatterns = [
   
   path('engineering/',views.engineering, name='engineering'),

]