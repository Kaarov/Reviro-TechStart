from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from config import permissions
from attributes import models
from attributes import serializers


class BeverageModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BeverageSerializer
    queryset = models.Beverage.objects.all()

    def get_permissions(self):
        if self.action in ('list', ):
            permission_classes = [permissions.ClientPermission]
        else:
            permission_classes = [permissions.PartnerPermission, permissions.AdminUserPermission]

        return [permission() for permission in permission_classes]


class SubscriptionModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SubscriptionSerializer
    queryset = models.Subscription.objects.all()


class OrderModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.PartnerPermission, permissions.AdminUserPermission]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class QRCodeModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QRCodeSerializer
    queryset = models.QRCode.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = [permissions.ClientPermission]
        else:
            permission_classes = [permissions.PartnerPermission, permissions.AdminUserPermission]

        return [permission() for permission in permission_classes]
