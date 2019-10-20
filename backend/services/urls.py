from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from services import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='SerCreate'),
    path('update', views.update, name="SerUpdate"),
    path('update/<int:id>', views.update, name="SerUpdate"),
    path('delete/<int:id>', views.delete, name="SerDelete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

