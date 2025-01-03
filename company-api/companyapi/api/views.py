from django.shortcuts import render
from api.models import Company
from rest_framework import viewsets 
from api.serializers import CompanySerializer 

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer