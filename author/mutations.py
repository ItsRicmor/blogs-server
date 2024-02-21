import graphene
from author.models import Author

from author.types import AuthorType


class CreateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        lastName = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, _, id, name, lastName):

        author = Author(id=id, name=name, lastName=lastName)
        author.save()
        return CreateAuthor(author=author)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        lastName = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, _, id, name=None, lastName=None):
        try:
            author = Author.objects.get(pk=id)
        except Author.DoesNotExist:
            raise Exception("Author not found")

        if name is not None:
            author.name = name
        if lastName is not None:
            author.lastName = lastName

        author.save()
        return UpdateAuthor(author=author)


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, _, id):
        try:
            author = Author.objects.get(pk=id)
        except Author.DoesNotExist:
            raise Exception("Author not found")

        author.delete()
        return DeleteAuthor(success=True)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
