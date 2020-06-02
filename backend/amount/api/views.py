from rest_framework import viewsets
from amount.models import Amount
from .serializers import AmountSerializer

class AmountViewSet(viewsets.ModelViewSet):
    serializer_class = AmountSerializer 
    queryset = Amount.objects.all()