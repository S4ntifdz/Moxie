from rest_framework import serializers
from service_management.models.service_type_model import ServiceTypeModel

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypeModel
        fields = '__all__'