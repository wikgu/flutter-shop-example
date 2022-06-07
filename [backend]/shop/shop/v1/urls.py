from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('users/login', views.Users.login, name='users'),
    path('users/create', views.Users.create, name='users'),
    path('users/logout', views.Users.logout, name='users'),
    path('users/get_user', views.Users.get_user, name='users'),
    path('users/delete', views.Users.delete, name='users'),
]