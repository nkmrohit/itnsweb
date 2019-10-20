from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='PorCreate'),
    path('update', views.update, name="PorUpdate"),
    path('update/<int:id>', views.update, name="PorUpdate"),
    path('delete/<int:id>', views.delete, name="PorDelete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

