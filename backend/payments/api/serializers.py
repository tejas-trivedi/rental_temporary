from rest_framework import serializers
from payments.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'made_by', 'made_on', 'amount', 'order_id')
        
        
        