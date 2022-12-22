from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_car, name='create_car'),
    path('delete/', views.delete_car, name='delete_car'),
    path('list/', views.CarListView.as_view(), name='car_list'),


]
