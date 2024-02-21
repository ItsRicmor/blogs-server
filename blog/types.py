from graphene_django import DjangoObjectType

from blog.models import Blog

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = "__all__"
