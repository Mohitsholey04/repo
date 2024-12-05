from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Order
        fields = '__all__'