from rest_framework import viewsets

from users.serializers import UserSerializer
from users.models import User

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer