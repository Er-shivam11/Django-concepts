from django.urls import path
from api import views

urlpatterns = [
    path('books/', views.BookList.as_view(),name='task2'),
    path('jwt/', views.JWTView.as_view(), name ='task4'),
    path('booklist/', views.booklist, name ='task3'),
]
