from rest_framework import routers
from .viewsets import RepuestosViewSet

router = routers.SimpleRouter()

router.register("api-repuestos",RepuestosViewSet)