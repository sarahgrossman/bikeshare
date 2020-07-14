from rest_framework import serializers
from bicycles.models import Bicycle

# Serializers define the API representation.


class BicycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bicycle
        fields = ['owner', 'nickname', 'id']