from rest_framework import viewsets
from medspas.models import MedspaModel
from api.serializers.medspas.medspa_serializer import MedspaSerializer

class MedspaView(viewsets.ModelViewSet):
    queryset = MedspaModel.objects.all()
    serializer_class = MedspaSerializer