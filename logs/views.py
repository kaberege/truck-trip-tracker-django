from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Trip
from .serializers import TripSerializer
from django.contrib.auth import get_user_model

User = get_user_model() # Custom user

# List/Create View for driver's daily trips
class TripListView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user  # Current authenticated user requesting the trip logs
        first_name = user.first_name  # Get the first_name of the authenticated user
        last_name = user.last_name  # Get the last_name of the authenticated user
        name =  first_name + ' ' + last_name  # Get full name

        # Fetch trip logs for the user
        results = Trip.objects.filter(user=user).order_by("-created_at")  # Get logs saved by the current user

        # Serializing user trip logs results
        user_logs_serializer = self.get_serializer(results, many=True)
        
        # Return a response with serialized data
        return Response( {
            'name': name,
            'trip_logs': user_logs_serializer.data
        }, status=status.HTTP_200_OK)

    # Overriding the perform_create method to add logic when creating a new trip
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # This associates the trip with the logged-in user

# Detail View for a single Trip, to Update (PUT/PATCH)
class TripDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Check if the user is the owner before updating
        if self.get_object().user != self.request.user:
            raise PermissionDenied("You can only update your own trip logs.")
        serializer.save()
    
    def perform_destroy(self, instance):
        # Check if the user is the owner before deleting
        if instance.user != self.request.user:
            raise PermissionDenied("You can only delete your own trip logs.")
        instance.delete()

