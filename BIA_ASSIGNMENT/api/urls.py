from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('books/', views.BookList.as_view(),name='task2'),
    path('jwt/', views.JWTView.as_view(), name ='task4'),
    path('booklist/', views.booklist, name ='task3'),
     path('merge_videos/', views.merge_videos, name='merge_videos'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)