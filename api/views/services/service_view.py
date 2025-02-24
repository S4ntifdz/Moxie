from rest_framework import viewsets
from api.serializers.services.service_serializer import ServiceSerializer
from service_management.models.service_model import ServiceModel

class ServiceView(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer