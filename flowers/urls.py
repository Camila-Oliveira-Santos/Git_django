from django.urls import path

from . import views

app_name = 'flowers'
urlpatterns = [
    path('', views.FlowerListView.as_view(), name='index'),
   # path('search/', views.search_flowers, name='search'),
    path('create/', views.create_flower, name='create'),
    path('<int:flower_id>/', views.detail_flower, name='detail'),
    path('update/<int:flower_id>/', views.update_flower, name='update'),
    path('delete/<int:flower_id>/', views.delete_flower, name='delete'),
   # path('<int:flower_id>/review/', views.create_review, name='review'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
]