from rest_framework import viewsets
from product.models import Product
from product.serializers import ProductSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
