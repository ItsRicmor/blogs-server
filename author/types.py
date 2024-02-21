from graphene_django import DjangoObjectType

from .models import Author

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"