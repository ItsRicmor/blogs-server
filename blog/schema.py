import graphene

from blog.types import BlogType

from .models import Blog

from .mutations import Mutation


class Query(graphene.ObjectType):
    blogs = graphene.List(BlogType)

    def resolve_blogs(self, _):
        return Blog.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)