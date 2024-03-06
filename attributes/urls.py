from rest_framework import routers
from attributes import views

router = routers.DefaultRouter()
router.register(
    "beverage", viewset=views.BeverageModelViewSet, basename="product"
)
router.register(
    "subscription", viewset=views.SubscriptionModelViewSet, basename="subscription"
)
router.register(
    "order", viewset=views.OrderModelViewSet, basename="order"
)
router.register(
    "qrcode", viewset=views.QRCodeModelViewSet, basename="qrcode"
)

urlpatterns = [
]

urlpatterns += router.urls
