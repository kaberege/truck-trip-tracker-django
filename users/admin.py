from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = User  # Tells Django that this admin is for the custom User model
    
    # List display in the admin panel
    list_display = (
        'email', 'first_name', 'last_name', 'username', 
        'is_staff'
    )
    
    # Fields to filter by in the admin panel
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    
    # Fields to search by in the admin panel
    search_fields = ('email', 'first_name', 'last_name')
    
    # Default ordering in the admin panel
    ordering = ('first_name', 'last_name',)


admin.site.register(User, CustomUserAdmin) # Register the custom user model with the custom admin interface
