from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # Custom user

# Trip model for storing daily driver trip details.
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    current_cycle_used = models.FloatField(blank=False, null=False)  
    route_estimated_distance = models.FloatField(blank=False, null=False, max_length=55)  # In meters 
    route_estimated_duration = models.FloatField(blank=False, null=False, max_length=55)  # In seconds 
    current_location_name = models.CharField(blank=False, null=False, max_length=255)
    pickup_location_name = models.CharField(blank=False, null=False, max_length=255)
    dropoff_location_name = models.CharField(blank=False, null=False, max_length=255)
    truck_number = models.CharField(blank=False, null=False, max_length=50)
    carried_product_name = models.CharField(blank=False, null=False, max_length=20)
    total_daily_miles = models.FloatField(blank=False, null=False, )
    duty_status = models.TextField(blank=False, null=False)
    driving_hours_0_11 = models.FloatField(default=0)
    driving_hours_12_17 = models.FloatField(default=0)
    driving_hours_18_23 = models.FloatField(default=0)
    off_duty_hours_0_11 = models.FloatField(default=0)
    off_duty_hours_12_17 = models.FloatField(default=0)
    off_duty_hours_18_23 = models.FloatField(default=0)
    on_duty_hours_0_11 = models.FloatField(default=0)
    on_duty_hours_12_17 = models.FloatField(default=0)
    on_duty_hours_18_23 = models.FloatField(default=0)
    sleeper_berth_hours_0_11 = models.FloatField(default=0)
    sleeper_berth_hours_12_17 = models.FloatField(default=0)
    sleeper_berth_hours_18_23 = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip from {self.current_location_name} to {self.dropoff_location_name} by {self.user}"