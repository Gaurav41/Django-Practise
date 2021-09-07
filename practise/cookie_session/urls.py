from django.urls import path
from cookie_session import views 


urlpatterns = [
   path('set_cookie', views.set_cookie),
   path('get_cookie', views.get_cookie),
   path('del_cookie', views.del_cookie),
   path('set_signed_cookie', views.set_signed_cookie_),
   path('get_signed_cookie', views.get_signed_cookie_),
   path('set_session', views.set_session),
   path('get_session', views.get_session),
   path('del_session', views.del_session),
   path('settestcookie', views.settestcookie),
   path('checktestcookie', views.checktestcookie),
   path('deltestcookie', views.deltestcookie),
  

]
