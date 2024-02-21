from graphene_django import DjangoObjectType

from .models import Series

class SeriesType(DjangoObjectType):
    class Meta:
        model = Series
        fields = "__all__"