from rest_framework import serializers
from driver.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ( 'qr_string', 'driverName', 
                  'NGO_id',
                   'contact_number', 'car_number')