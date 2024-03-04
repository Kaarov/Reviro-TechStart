from rest_framework import viewsets
from establishment.models import Establishment
from establishment.serializers import EstablishmentSerializer


class EstablishmentModelViewSet(viewsets.ModelViewSet):
    serializer_class = EstablishmentSerializer
    queryset = Establishment.objects.all()
