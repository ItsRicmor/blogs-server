import graphene

from .mutations import Mutation
from .types import SeriesType
from .models import Series

class Query(graphene.ObjectType):
    seriess = graphene.List(SeriesType)

    def resolve_seriess(self, _):
        return Series.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)