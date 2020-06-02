from django.db import models
from status.models import NGO
from django.conf import settings
import uuid

class Trip(models.Model):
    order_id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    NGO_id = models.ForeignKey(NGO, default=1, on_delete=models.CASCADE)
    #NGO_name = models.ForeignKey(NGO, default='user', on_delete=models.CASCADE)
    driverName = models.CharField(max_length=50, blank=True)     # this driver name will come from QR string
    timestamp = models.DateTimeField(auto_now_add=True)
   
  #  def __int__(self):
   #     return self.user
    def __str__(self):
        return '{}{}'.format(self.NGO_id, self.user)
      
      
      
      # merchant id, merchant key, timestamp in NGO model ......  Amount database   timestamp,trip id, order id, merchant id and key of specific ngo, transaction id, status, user,
      # patch for ngo selection  