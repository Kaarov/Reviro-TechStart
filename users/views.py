from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users import models
from users import serializers


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return super().get_queryset().filter(username=self.request.user.username)


class ProfileUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return super().get_queryset().filter(username=self.request.user.username)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ChangePasswordSerializer

    def post(self, request):
        serializer = serializers.ChangePasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.update_password(serializer.validated_data)
        return Response({"msg": "Password is updated"}, status=status.HTTP_200_OK)
