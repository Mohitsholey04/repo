from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = User
        fields = '__all__'