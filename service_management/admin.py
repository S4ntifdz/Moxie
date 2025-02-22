from django.contrib import admin

from service_management.models import ServiceModel

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','price',]