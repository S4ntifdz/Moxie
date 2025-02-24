from rest_framework import viewsets
from api.serializers.services.service_category_serializer import ServiceCategorySerializer
from api.serializers.services.service_type_serializer import ServiceTypeSerializer
from service_management.models.service_category_model import ServiceCategoryModel


class ServiceCategoryView(viewsets.ModelViewSet):
    queryset = ServiceCategoryModel.objects.all()
    serializer_class = ServiceCategorySerializer