from rest_framework import serializers
from status.models import NGO


class NgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = [  
            'NGO_id', 'name','location',
            'type', 'description', 'contact_number',
        ]

class NgoNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = [ 
            'name',
        ]


