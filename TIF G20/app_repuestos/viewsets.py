


from rest_framework.viewsets import ModelViewSet
from .models import Repuestos 
from .serializers import RepuestosSerializer 

class RepuestosViewSet(ModelViewSet):
    queryset = Repuestos.objects.all()
    serializer_class = RepuestosSerializer
