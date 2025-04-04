from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterUserView, LoginUserView, UserUpdateView, UserDeleteView

urlpatterns = [
    # User registration, login, update, and delete paths
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('delete/', UserDeleteView.as_view(), name='delete'),

    # JWT token paths
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
