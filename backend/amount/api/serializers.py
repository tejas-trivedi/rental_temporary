from rest_framework import serializers
from amount.models import Amount


class AmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amount
        fields = ('id', 'user', 'NGO_id', 'transaction_id', 'timestamp', 'amount', 'status')