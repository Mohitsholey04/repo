from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'