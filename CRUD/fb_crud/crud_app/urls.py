from django.urls import path

# importing views from views..py
from crud_app import views
from django.contrib import admin

urlpatterns = [
	path('', views.create_view ),
	path('list/', views.list_view ),
]
# http://127.0.0.1:8000/admin/crud_app/shivambytes/