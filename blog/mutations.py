import graphene

from author.models import Author

from .types import BlogType
from .models import Blog

class CreateBlog(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        author_id = graphene.ID(required=True)

    blog = graphene.Field(BlogType)

    def mutate(self, _, title, content, author_id):

        author = Author.objects.get(pk=author_id)
        blog = Blog(title=title, content=content, author=author)
        blog.save()
        return CreateBlog(blog=blog)


class UpdateBlog(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        author_id = graphene.ID(required=True)

    blog = graphene.Field(BlogType)

    def mutate(self, _, id, title=None, content=None, author_id=None):
        try:
            blog = Blog.objects.get(pk=id)
        except Blog.DoesNotExist:
            raise Exception("Blog not found")

        if title is not None:
            blog.title = title
        if content is not None:
            blog.content = content
        if author_id is not None:
            author = Author.objects.get(pk=author_id)
            blog.author = author

        blog.save()
        return UpdateBlog(blog=blog)


class DeleteBlog(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, _, id):
        try:
            blog = Blog.objects.get(pk=id)
        except Blog.DoesNotExist:
            raise Exception("Blog not found")

        blog.delete()
        return DeleteBlog(success=True)
    

class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    update_blog = UpdateBlog.Field()
    delete_blog = DeleteBlog.Field()