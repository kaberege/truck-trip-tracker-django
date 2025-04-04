from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    user= serializers.PrimaryKeyRelatedField(read_only=True)
    
    # Serializing 'created_at' and 'updated_at' as ISO format date-time strings
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S', read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'

