from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from users.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password",)
        filter_fields = ['is_staff']
        interfaces = (relay.Node,)


class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
