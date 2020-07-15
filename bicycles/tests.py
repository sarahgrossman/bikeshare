from django.test import TestCase
from rest_framework.test import APIClient

from bicycles.models import Bicycle
from users.models import User

# Create your tests here.


class BicycleViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin', email='test@test.com', is_staff=True, is_superuser=True)
        self.client = APIClient()
        self.bicycle = Bicycle.objects.create(nickname="test bike", owner=self.user)
        self.bicycle_2 = Bicycle.objects.create(nickname="other bike", owner=self.user)

    def test_get_returns_all_bicycles(self):
        resp = self.client.get('/bicycles')
        assert len(resp.json()) == 2
        assert resp.json()[0]['owner'] == self.user.id

    def test_search_nickname_returns_matches(self):
        resp = self.client.get('/bicycles?search=test', content_type='application/json')
        print(resp)
        assert len(resp.json()) == 1
        assert resp.json()[0]['nickname'] == self.bicycle.nickname