from rest_framework import viewsets

from config.permissions import GuestPermission
from config.permissions import PartnerPermission
from config.permissions import AdminUserPermission

from product.models import Product
from product.serializers import ProductSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [GuestPermission]
        else:
            permission_classes = [PartnerPermission, AdminUserPermission]

        return [permission() for permission in permission_classes]
