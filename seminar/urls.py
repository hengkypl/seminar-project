from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import majelis.views
import peserta.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', majelis.views.home, name='home'),
    path('peserta/', include('peserta.urls')),
    path('blog/', include('blog.urls')),
    path('about/', majelis.views.about, name='about'),
    path('register/', peserta.views.register, name='register'),

]
