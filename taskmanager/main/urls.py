from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('admin', views.admin, name='admin'),
    path('admin/', views.about, name='admin_console'),
    path('create', views.create, name='create')
]
