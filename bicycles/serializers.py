from rest_framework import serializers
from bicycles.models import Bicycle

# Serializers define the API representation.


class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = '__all__'
