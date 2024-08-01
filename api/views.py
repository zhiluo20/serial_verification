from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import SerialNumber

@api_view(['POST'])
def validate_serial(request):
    serial = request.data.get('serial')
    try:
        serial_number = SerialNumber.objects.get(serial=serial)
        if datetime.now().date() < serial_number.expiry_date:
            return Response({"valid": True, "expiry_date": serial_number.expiry_date}, status=status.HTTP_200_OK)
        else:
            return Response({"valid": False, "message": "Serial number has expired."}, status=status.HTTP_400_BAD_REQUEST)
    except SerialNumber.DoesNotExist:
        return Response({"valid": False, "message": "Invalid serial number."}, status=status.HTTP_400_BAD_REQUEST)