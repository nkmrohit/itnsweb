from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from feedback import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='FeeCreate'),
    path('update', views.update, name="FeeUpdate"),
    path('update/<int:id>', views.update, name="FeeUpdate"),
    path('delete/<int:id>', views.delete, name="FeeDelete"),
    # path('list', views.list, name='list'),
    # path('details/<int:product_id>', views.details, name="details"),
    # path('edit/<int:product_id>', views.edit, name="edit"),
    # path('delete/<int:product_id>', views.delete, name="delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

