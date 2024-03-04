from rest_framework import routers

from product.views import ProductModelViewSet

router = routers.DefaultRouter()
router.register(
    "", viewset=ProductModelViewSet, basename="product"
)

urlpatterns = []

urlpatterns += router.urls
