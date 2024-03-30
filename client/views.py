from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientInvoiceSerializer
from .models import Client

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientInvoiceSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
