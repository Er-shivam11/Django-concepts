from django.urls import path

# importing views from views..py
from crud_app import views
from django.contrib import admin

urlpatterns = [
	path('', views.create_view,name='home' ),
	path('list/', views.list_view ,name='list'),
    path('update/<int:pk>/', views.update_view, name='update_view'),
    path('delete/<int:pk>/', views.delete_view, name='delete_view'),
]
# http://127.0.0.1:8000/admin/crud_app/shivambytes/