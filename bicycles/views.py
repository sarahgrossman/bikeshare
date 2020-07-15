from rest_framework import viewsets, filters


from bicycles.serializers import BicycleSerializer
from bicycles.models import Bicycle
from users.permissions import IsOwnerOrAdmin

# Create your views here.


class BicycleViewSet(viewsets.ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nickname']
    permission_classes = [IsOwnerOrAdmin]
