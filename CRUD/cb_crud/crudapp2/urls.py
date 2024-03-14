from django.urls import path

# importing views from views..py
from crudapp2 import views
from django.contrib import admin

urlpatterns = [
	path('', views.AddandShowView.as_view(),name='home' ),
	path('list/', views.list_view ,name='list'),
    path('update/<int:id>/', views.UpdateView.as_view(), name='update_view'),
    path('delete/<int:id>/', views.DeleteView.as_view(), name='delete_view'),
]
# http://127.0.0.1:8000/admin/crud_app/shivambytes/