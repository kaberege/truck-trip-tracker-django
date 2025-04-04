from django.contrib import admin
from .models import Trip

class TripAdmin(admin.ModelAdmin):
    # List display that defines which fields will be shown in the list view
    list_display = (
        'user', 
        'current_cycle_used', 
        'route_estimated_distance', 
        'route_estimated_duration', 
        'current_location_name', 
        'pickup_location_name', 
        'dropoff_location_name', 
        'truck_number', 
        'carried_product_name', 
        'total_daily_miles', 
        'duty_status', 
        'created_at', 
        'updated_at'
    )
    
    # Search fields to allow searching through specific fields in the admin interface
    search_fields = (
        'user__username',  # Can search by username if using custom User model
        'current_location_name', 
        'pickup_location_name', 
        'dropoff_location_name', 
        'truck_number', 
        'carried_product_name'
    )
    
    # Filter options to narrow down results based on certain criteria
    list_filter = ('created_at', 'updated_at', 'user')

# Register the Trip model with the TripAdmin class
admin.site.register(Trip, TripAdmin)
