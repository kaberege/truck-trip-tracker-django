from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer, LoginSerializer, UserProfileUpdateSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()  # Custom user model

# Handle user registration requests
class RegisterUserView(views.APIView):
    def post(self, request):
        # Initialize the serializer with the provided request data
        serializer = RegistrationSerializer(data=request.data)
        
        # Check if the data is valid according to the serializer's validation logic
        if serializer.is_valid():
            # Save the new user to the database if the data is valid
            serializer.save()
            
            # Return a success message with HTTP status 201 (Created)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        
        # If the serializer data is invalid, return the validation errors with HTTP status 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handle user login requests
class LoginUserView(views.APIView):
    def post(self, request):
        # Initialize the login serializer with the provided request data
        serializer = LoginSerializer(data=request.data)

        # Check for data validation
        if not serializer.is_valid():
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
    
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
    
        # Attempt to authenticate the user
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                # Create JWT token
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                # Return the tokens
                return Response({'access': str(access_token),'refresh': str(refresh)})
            else:
                return Response({"error": "Invalid email or password!"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password!"}, status=status.HTTP_400_BAD_REQUEST)

# Handle user update logic
class UserUpdateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        instance = request.user
        serializer = UserProfileUpdateSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()   # Update the user
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handle user delete logic
class UserDeleteView(views.APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        instance = request.user
        instance.delete()  # Delete the user

        return Response({"message": "User has been deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


