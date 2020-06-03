from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from status.models import NGO

class Driver(models.Model):
    
    qr_string = models.CharField(primary_key=True,max_length=120, default='0010')
    driverName = models.CharField(max_length=50, blank=True)
    car_number = models.CharField(max_length=13)
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Enter a 10 digit mobile number', code='nomatch')], null=True)
    #NGO_id = models.ForeignKey(NGO, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.driverName  
  #  def __int__(self):
    #     return self.user
    