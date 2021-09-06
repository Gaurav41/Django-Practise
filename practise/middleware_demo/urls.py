from django.urls import path
# from form_demo import views 
from middleware_demo import views

urlpatterns = [
   path('', views.index),
   path('user', views.user_info),
   path('view_err', views.view_err),
]