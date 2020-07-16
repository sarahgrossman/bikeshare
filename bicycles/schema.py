from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from bicycles.models import Bicycle


class BicycleNode(DjangoObjectType):
    class Meta:
        model = Bicycle
        filter_fields = {
            'nickname': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    bicycle = relay.Node.Field(BicycleNode)
    all_bicycles = DjangoFilterConnectionField(BicycleNode)

