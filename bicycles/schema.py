import graphene
from graphene_django.types import DjangoObjectType

from bicycles.models import Bicycle


class BicycleType(DjangoObjectType):
    class Meta:
        model = Bicycle


class Query(object):
    all_bicycles = graphene.List(BicycleType)

    def resolve_all_bicycles(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Bicycle.objects.select_related('user').all()
