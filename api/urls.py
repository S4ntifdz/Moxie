from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.appointment.appointment_view import AppointmentView
from api.views.medspas.medspa_view import MedspaView


router = DefaultRouter()
router.register(r'medspas', MedspaView)
router.register(r'appointments', AppointmentView)

urlpatterns = [
    path('', include(router.urls)),
]