from django.db import models

from medspas.models import MedspaModel

class ServiceModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    medspa = models.ForeignKey(MedspaModel, on_delete=models.CASCADE)
    
    class Meta:
            verbose_name = "Service"
            verbose_name_plural = "Services"

    def __str__(self):
        return self.name
    
