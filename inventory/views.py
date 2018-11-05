# from django.http import HttpResponse
# from django.shortcuts import render

from inventory.models import Inventory
from rest_framework import viewsets

from green_trade.serializers import InventorySerializer


class StrainsView(viewsets.ModelViewSet):
    ''' the main entry point for thew api '''
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
