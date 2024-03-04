from rest_framework import routers

from establishment.views import EstablishmentModelViewSet

router = routers.DefaultRouter()
router.register(
    "", viewset=EstablishmentModelViewSet, basename="establishment"
)

urlpatterns = []

urlpatterns += router.urls
