from rest_framework import serializers
from api.models import Company

# create Serealizer class for Company model
class ComapnySerealizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'