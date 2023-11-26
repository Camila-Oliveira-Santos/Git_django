from django.urls import path

from . import views

app_name = 'flowers'
urlpatterns = [
    path('', views.list_flowers, name='index'),
    path('search/', views.search_flowers, name='search'),
    path('create/', views.create_flower, name='create'),
    path('<int:flower_id>/', views.detail_flower, name='detail'),
]