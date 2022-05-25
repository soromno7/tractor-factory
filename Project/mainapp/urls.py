from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('vote', views.vote, name='vote'),
    path('part', views.part, name='part'),
    path('part_ordered_name', views.part_ordered_name, name='part_ordered_name'),
    path('part_ordered_price', views.part_ordered_price, name='part_ordered_price'),
    path('part_filtrated', views.part_filtrated, name='part_filtrated'),
    path('kondorse', views.kondorse, name='kondorse'), 
]