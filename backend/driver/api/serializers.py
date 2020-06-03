from rest_framework import serializers
from driver.models import Driver
from status.models import NGO

class DriverSerializer(serializers.ModelSerializer):
    Ngo_name = {}
    Ngo_name = serializers.SerializerMethodField()
    class Meta:
        model = Driver
        fields = ('driverName','Ngo_name')
    def get_Ngo_name(self, obj):
        list_ngo = NGO.objects.values_list('name', flat=True)
        return list_ngo

"""
from rest_framework import serializers
from driver.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ( 'qr_string', 'driverName', 
                  'NGO_id',
                   'contact_number', 'car_number')
"""