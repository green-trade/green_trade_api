from django.test import TestCase
# from django.urls import resolve
from rest_framework.test import APIRequestFactory

from inventory.views import StrainsView

import re
import uuid
import json
from datetime import datetime


from inventory.models import Inventory


class TestBaseStrains(TestCase):
    def setUp(self):
        super().setUp()
        self.default_data = list()

        self.factory = APIRequestFactory()

        self.make_invintory_db()

    def get_api_strains(self, get_obj=None, pk=None):
        if get_obj and pk:
            strains_view = StrainsView.as_view(get_obj)
        elif get_obj and not pk:
            raise Exception('needs both a object and a pk')
        elif pk and not get_obj:
            raise Exception('needs both a object and a pk')
        else:
            strains_view = StrainsView.as_view({'get': 'list'})

        request = self.factory.get("")

        if pk:
            return strains_view(request, pk=pk)
        else:
            return strains_view(request)

    def make_invintory_db(self):
        default_data = [{
            'id': uuid.uuid4(),
            'created_at': datetime.now(),
            'last_edited': datetime.now(),
            'name': 'test strain',
            'provider': 'test provider',
            'thc_percent': 10,
            'cbd_percent': 10,

            },
            {'id': uuid.uuid4(),
             'created_at': datetime.now(),
             'last_edited': datetime.now(),
             'name': 'test two',
             'provider': 'test provider',
             'thc_percent': 10,
             'cbd_percent': 10,
             }]

        for data in default_data:
            obj = Inventory.objects.create(
                    id=data['id'],
                    created_at=data['created_at'],
                    last_edited=data['last_edited'],
                    name=data['name'],
                    provider=data['provider'],
                    thc_percent=data['thc_percent'],
                    cbd_percent=data['cbd_percent'],)

            obj.save()

            self.default_data.append(obj)

    def test_get_strains(self):
        get_request = self.get_api_strains()

        self.assertEqual(get_request.status_code, 200)

    def test_get_a_strain_with_uuid(self):
        pk = self.default_data[0].pk

        get_request = self.get_api_strains(
                get_obj={'get': 'retrieve'}, pk=pk)

        self.assertEqual(get_request.status_code, 200)
