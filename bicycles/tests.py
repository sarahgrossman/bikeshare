from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from bicycles.models import Bicycle
from users.models import User

# Create your tests here.


class BicycleViewsTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username="admin", email="test@test.com", is_staff=True, is_superuser=True)
        self.non_admin = User.objects.create(username="non_admin", email="test@test.com", is_staff=True, is_superuser=True)
        self.admin_client = APIClient()
        admin_token, created = Token.objects.get_or_create(user=self.admin)
        self.admin_client.credentials(HTTP_AUTHORIZATION='Token ' + admin_token.key)
        self.bicycle = Bicycle.objects.create(nickname="admin's awesome bike", owner=self.admin)
        self.bicycle_2 = Bicycle.objects.create(nickname="admin's second bike", owner=self.admin)
        self.bicycle_3 = Bicycle.objects.create(nickname="non admin's awesome bike", owner=self.non_admin)

    def test_get_returns_all_bicycles(self):
        resp = self.admin_client.get('/bicycles')
        assert len(resp.json()) == 3
        assert resp.json()[0]['owner'] == self.admin.id

    def test_search_nickname_returns_matches(self):
        resp = self.admin_client.get('/bicycles?search=second')
        assert len(resp.json()) == 1
        assert resp.json()[0]['nickname'] == self.bicycle_2.nickname
    
    def test_admin_can_edit_non_admin_bike(self):
        resp = self.admin_client.patch(f"/bicycles/{self.bicycle_3.id}", {"nickname": "non admin's okay bike"}, format='json')
        assert resp.json()["nickname"] == "non admin's okay bike"