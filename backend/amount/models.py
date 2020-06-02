from django.db import models
from status.models import NGO
from trip.models import Trip
from django.conf import settings
import uuid

class Amount(models.Model):
    
    ORDER_STATUS = (
        (0, "Pending"),
        (1, "Done"),
        (2, "Failed"),
    )
    
    #trip_id = models.ForeignKey(Trip, default = uuid.uuid4, editable = False, on_delete= models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    NGO_id = models.ForeignKey(NGO, default=1, on_delete=models.CASCADE)
    merchant_id = models.CharField(max_length=20)
    merchant_key = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    status = models.IntegerField(choices=ORDER_STATUS, default=0)
    
   
    def __str__(self):
        return self.transaction_id
      
    
      
    # merchant id, merchant key, timestamp in NGO model ......  Amount database   timestamp,trip id, order id, merchant id and key of specific ngo, transaction id, status, user,
    # patch for ngo selection  