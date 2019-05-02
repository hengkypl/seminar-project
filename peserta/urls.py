from django.urls import path
from . import views


urlpatterns = [
    path('', views.pesertahome, name='pesertahome'),
    path('register/', views.register, name='register'),
]
