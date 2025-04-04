from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom manager for user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Ensure email is provided
        if not email:
            raise ValueError("Email is required!")
        user = self.model(email=self.normalize_email(email), **extra_fields) # Set & normalize email address
        user.set_password(password)  # Set the password
        user.save(using=self._db)  # Save the user to the database

        return user

    def create_superuser(self, email, password=None, **extra_fields ):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)  # Save the superuser to the database

        # Call create_user to handle superuser creation
        return user


# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False, max_length=255) # Email is unique and required
    username = models.CharField(unique=False, max_length=25)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # Specify the fields that are required when creating a user (excluding the username)
   
    objects = CustomUserManager()  # Custom manager for handling user creation

    def __str__(self):
        return f' {self.first_name} {self.last_name}'