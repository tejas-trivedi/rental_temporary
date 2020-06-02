from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

class NGOQuerySet(models.QuerySet):
    pass

class NGOManager(models.Manager):
    def get_queryset(self):
        return NGOQuerySet(self.model,using=self._db)


# Create your models here.
class NGO(models.Model):
    
    NGO_TYPES = (
		("None", "Choose an option"),
		("Profit", "Profit"),
		("Non Profit", "Non Profit"),
		("Charitable Oriented", "Charitable Oriented"),
		("Empowerment Oriented", "Empowerment Oriented") 
    )
    
    NGO_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.TextField()
    type = models.CharField( choices=NGO_TYPES, default= "None", max_length=20)
    description = models.TextField()
    merchant_id = models.CharField(max_length=20)
    merchant_key = models.CharField(max_length=20)
    NGO_website = models.URLField(max_length=100)
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Enter a 10 digit mobile number', code='nomatch')], null=True)
    

    objects = NGOManager()

    def __str__(self):
        return '{}{}'.format(self.NGO_id, self.name)
    # def __str__(self):
    #     return self.NGO_name