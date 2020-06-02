from rest_framework import viewsets
from trip.models import Trip
from .serializers import TripSerializer#, LocationSerializer
from django.contrib.auth.models import User
from status.register.serializers import UserSerializer

class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer 
    queryset = Trip.objects.all()

    
#class LocationViewSet(viewsets.ModelViewSet):
#    serializer_class = LocationSerializer
#    queryset = Trip.objects.all()
