from django.urls import path
from .views import validate_serial

urlpatterns = [
    path('validate/', validate_serial, name='validate_serial'),
]