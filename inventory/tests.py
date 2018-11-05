from django.test import TestCase
from rest_framework.test import APIRequestFactory

from inventory.models import Inventory


class TestBaseStrains(TestCase):
    def setUp(self):
        super().setUp()

        self.factory = APIRequestFactory()

    def make_invintory_db():
        default_obj = {
                'name': 'test strain',
                'provider': 'test provider',
                'thc_percent': 10,
                'cbd_percent': 10,
                }

        inventory_default = Inventory(**default_obj)

        inventory_default.save()

    def api_get(self):
        return self.factory.get('/strains/', {}, format='get')

    def test_get_strains(self):
        get_request = self.api_get()

        import ipdb; ipdb.set_trace()  # noqa

