from django.urls import path
from file_upload import views 


urlpatterns = [
   path('', views.index),
]
