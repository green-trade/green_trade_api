# from django.http import HttpResponse
# from django.shortcuts import render

from inventory.models import Inventory
from rest_framework import viewsets

from green_trade.serializers import InventorySerializer


class IndexView(viewsets.ModelViewSet):
    '''
    api for nothing fools
    '''

    queryset = Inventory.objects.all()[:5]
    serializer_class = InventorySerializer
