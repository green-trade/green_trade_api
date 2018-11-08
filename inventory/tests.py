from django.test import TestCase
# from django.urls import resolve
from rest_framework.test import APIRequestFactory

from inventory.views import StrainsView

import uuid
from datetime import datetime


from inventory.models import Inventory


class TestBaseStrains(TestCase):
    def setUp(self):
        super().setUp()
        self.default_data = list()

        self.factory = APIRequestFactory()

        self.make_invintory_db()

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
        strains_view = StrainsView.as_view({'get': 'list'})

        request = self.factory.get("")

        get_request = strains_view(request)

        self.assertEqual(get_request.status_code, 200)

    def test_get_a_strain_with_uuid(self):
        pk = self.default_data[0].pk

        strains_view = StrainsView.as_view({'get': 'retrieve'})

        request = self.factory.get("")

        get_request = strains_view(request, pk=pk)

        self.assertEqual(get_request.status_code, 200)
