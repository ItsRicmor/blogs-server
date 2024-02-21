import graphene
from .models import Author
from .mutations import Mutation

from .types import AuthorType


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)

    def resolve_authors(self, _):
        return Author.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)