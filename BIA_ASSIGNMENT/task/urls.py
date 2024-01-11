from django.urls import path
from task import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('task1', views.hello,name='task1'),
    path('', views.home,name='home'),
    path('login/', views.loginuser, name='login'),
    path('movie/', views.movie, name='movie'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)