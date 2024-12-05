from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'



        