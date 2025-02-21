import uuid
from django.db import models

from services.models import ServiceModel
from medspas.models import MedspaModel


class AppointmentStatus(models.TextChoices):
     SCHEDULED = 'Scheduled'
     COMPLETED = 'Completed'
     CANCELED = 'Canceled'

class AppointmentModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField(blank=False, null=False)
    total_duration = models.IntegerField()
    total_price = models.IntegerField()
    medspa = models.ForeignKey(MedspaModel, on_delete=models.CASCADE)
    services = models.ManyToManyField(ServiceModel)

    class Meta:
            verbose_name = "Appointment"
            verbose_name_plural = "Appointments"

    def __str__(self):
        return self.name
    
