from rest_framework import serializers

from attributes import models


class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beverage
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QRCode
        fields = "__all__"
