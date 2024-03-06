from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from users.views import RegisterUserAPIView, ChangePasswordView
from users.views import ProfileListAPIView
from users.views import ProfileUpdateDestroyAPIView

urlpatterns = [
    path("profile/", ProfileListAPIView.as_view(), name="profile_list"),
    path("profile/<int:id>/", ProfileUpdateDestroyAPIView.as_view(), name="profile_update_delete"),
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]
