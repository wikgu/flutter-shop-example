from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>', views.details, name='products'),
    path('users/login', views.Users.login, name='users'),
    path('users/create', views.Users.create, name='users'),
    path('users/logout', views.Users.logout, name='users'),
    path('users/details', views.Users.details, name='users'),
    path('users/delete', views.Users.delete, name='users'),
]