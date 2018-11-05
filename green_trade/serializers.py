# from django.contrib.auth.models import (User, Group)

from inventory.models import Inventory
from rest_framework import serializers


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    ''''''
    class Meta:
        model = Inventory
        fields = ('url',
                  'created_at',
                  'last_edited',
                  'name',
                  'thc_percent',
                  'cbd_percent'
                  )
