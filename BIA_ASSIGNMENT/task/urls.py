from django.urls import path
from task import views

urlpatterns = [
    path('task1', views.hello,name='task1'),
    path('', views.home,name='home'),
    path('login/', views.loginuser, name='login'),
    path('movie/', views.movie, name='movie'),

]
