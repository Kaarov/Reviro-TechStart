from rest_framework import serializers

from establishment.models import Establishment


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        exclude = ("created_at", "updated_at")
