from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pesertahome, name='pesertahome'),
    path('register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
