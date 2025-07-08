from django.urls import path
from . import views
urlpatterns = [
   path('insert_faculty/',views.insert_faculty,name='insert_faculty'),
    # other paths as needed
]