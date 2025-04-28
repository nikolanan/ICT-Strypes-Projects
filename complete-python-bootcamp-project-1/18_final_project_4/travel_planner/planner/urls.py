from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_itinerary/', views.create_itinerary, name='create_itinerary'),
    path('create_airline/', views.create_airline, name='create_airline'),
    path('create_hotel/', views.create_hotel, name='create_hotel'),
    path('create_point_of_interest/', views.create_point_of_interest, name='create_point_of_interest'),
]
