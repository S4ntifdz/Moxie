from rest_framework import viewsets
from api.serializers.services.service_type_serializer import ServiceTypeSerializer
from service_management.models.service_type_model import ServiceTypeModel


class ServiceTypeView(viewsets.ModelViewSet):
    queryset = ServiceTypeModel.objects.all()
    serializer_class = ServiceTypeSerializer