from django.urls import path
from .views import TripListView, TripDetailView

urlpatterns = [
    path('trips/', TripListView.as_view(), name='trip-list'),  # for listing and creating trips
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),  # for retrieving, updating, and deleting a specific trip
]
