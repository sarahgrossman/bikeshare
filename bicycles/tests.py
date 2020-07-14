from django.test import TestCase
from rest_framework.test import APIClient

from bicycles.models import Bicycle
from users.models import User

# Create your tests here.


class BicycleViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin', email='test@test.com', is_staff=True, is_superuser=True)
        self.client = APIClient()        
        self.bicycle = Bicycle.objects.create(nickname="lion", owner=self.user)

    def test_get_returns_all_bicycles(self):
        resp = self.client.get('/bicycles/')
        assert len(resp.json()) == 1
        assert resp.json()[0]['owner'] == self.user.id
