from django.urls import path
from file_upload import views 


urlpatterns = [
   path('', views.index),
   path('book_list', views.book_list),
   path('upload_book', views.upload_book),
   path('delete_book/<int:pk>', views.delete_book,name='delete_book'),

]
