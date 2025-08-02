from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('products', views.products, name = 'products'),
    path('contactus', views.contactus, name = 'contactus'),
    path('index', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.delete_post, name='delete'),
    path('create/', views.create_post, name='create'),
    path('update/<int:id>', views.update_post, name='update'),
]
