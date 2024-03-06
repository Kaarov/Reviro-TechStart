from rest_framework import viewsets

from config.permissions import GuestPermission
from config.permissions import PartnerPermission
from config.permissions import AdminUserPermission

from establishment.models import Establishment
from establishment.serializers import EstablishmentSerializer


class EstablishmentModelViewSet(viewsets.ModelViewSet):
    serializer_class = EstablishmentSerializer
    queryset = Establishment.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [GuestPermission]
        else:
            permission_classes = [PartnerPermission, AdminUserPermission]

        return [permission() for permission in permission_classes]
