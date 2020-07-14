from rest_framework import viewsets

from bicycles.serializers import BicycleSerializer
from bicycles.models import Bicycle

# Create your views here.


class BicycleViewSet(viewsets.ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
