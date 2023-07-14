from rest_framework.serializers import ModelSerializer 
from .models import Repuestos

class RepuestosSerializer(ModelSerializer):
    class Meta:
     model = Repuestos
    fields = "__all__"