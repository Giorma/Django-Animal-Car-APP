from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_animal, name='create_animal'),
    path('delete/', views.delete_animal, name='delete_animal'),
    path('list/', views.AnimalListView.as_view(), name='animal_list'),


]
