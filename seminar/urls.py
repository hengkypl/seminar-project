from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import majelis.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', majelis.views.home, name='home'),
    path('about/', majelis.views.about, name='about'),

]
