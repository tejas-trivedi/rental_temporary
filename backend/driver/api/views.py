from rest_framework import generics
from driver.models import Driver
#from status.models import NGO
from .serializers import DriverSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 

class QRDetail(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'qr_string'

"""
from rest_framework import viewsets
from driver.models import Driver
from .serializers import DriverSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer 
    queryset = Driver.objects.all()
    
   # permission_classes = [IsAuthenticated]
   # 
   # def get(self, request, format=None):
   #     content = {
   #         'status': 'request was permitted'
   #     }
   #     return Response(content)
"""
    

