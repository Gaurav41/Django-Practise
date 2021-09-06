
from django.urls import path
from manage_static_files import views 

urlpatterns = [
   path('', views.index),
   
]
