from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from about import views


urlpatterns = [
    path('', views.index, name='index'),
    path('seo', views.seo, name='CapSeo'),
    path('GoogleTrendsSlopeCalculator', views.GoogleTrendsSlopeCalculator, name='GoogleTrendsSlopeCalculator'),
    path('test', views.test, name='test'),
    # path('update', views.update, name="CapUpdate"),
    # path('update/<int:id>', views.update, name="CapUpdate"),
    # path('delete/<int:id>', views.delete, name="CapDelete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

