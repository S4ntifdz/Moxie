from django import forms
from django.contrib import admin
from appointments.models import AppointmentModel
from service_management.models import ServiceModel

class appointmentCustomForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=ServiceModel.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    class Meta:
        models = AppointmentModel
        fields = '__all__'

@admin.register(AppointmentModel)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('medspa','total_price', 'total_duration',)

    def get_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    get_services.short_description = 'Services'