from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model() # Custom user

    # Serializer for user registration
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

       # Override the create method to handle user creation logic
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user # Return the created user instance
     
    # Serializer for user login
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    

    # Serializer for updating a user
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def update(self, instance, validated_data):

        # Pop the password field from validated_data to handle separately
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        # Save the instance
        instance.save()
        return instance
