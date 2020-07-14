from rest_framework import serializers

from bicycles.serializers import BicycleSerializer
from users.models import User


# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    bicycles = BicycleSerializer(many=True, read_only=True, source='bicycle_set')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'id', 'bicycles']
