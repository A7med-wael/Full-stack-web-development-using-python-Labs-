from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='category.index'),
    path('details/<int:pk>', views.details, name='category.details'),
    path('create', views.create_category, name='category.create'),
    path('update/<int:pk>', views.update_category, name='category.update'),
    path('delete/<int:pk>', views.delete_category, name='category.delete'),
]