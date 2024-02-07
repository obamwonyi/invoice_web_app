from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializers
from .models import Client

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializers
    queryset = Client.objects.all()

    
    def get_queryset(self):
        """
        This will filter the response to only include 
        the data that are created by the current user 
        """
        return self.queryset.filter(created_by=self.request.user)
    