from rest_framework import serializers
from trip.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('trip_id', 'user', 'NGO_id', 'driverName', 'timestamp')
        
#class LocationSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Trip
#        fields = ('trip_id', 'startingLocation', 'destination')
        