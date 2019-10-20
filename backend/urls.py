
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', include('authuser.urls')),
    url('capability/', include('capability.urls')),
    url('portfolio/', include('portfolio.urls')),
    url('slider/', include('slider.urls')),
    url('services/', include('services.urls')),
    url('feedback/', include('feedback.urls')),
    url('setting/', include('setting.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

