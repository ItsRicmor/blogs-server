import graphene
from graphene_django import DjangoObjectType

from blog.models import Blog
from .models import Series

class SeriesType(DjangoObjectType):
    class Meta:
        model = Series
        fields = "__all__"


class CreateSeries(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        blogs_id = graphene.List(graphene.ID, required=True)

    series = graphene.Field(SeriesType)

    def mutate(self, _, title, blogs_id):

        blogs = Blog.objects.filter(pk__in=blogs_id)
        series = Series(title=title, blogs=blogs)

        series.save()
        return CreateSeries(series=series)


class UpdateSeries(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        blogs_id = graphene.List(graphene.ID, required=True)

    series = graphene.Field(SeriesType)

    def mutate(self, _, id, title=None, blogs_id=None):
        try:
            series = Series.objects.get(pk=id)
        except Series.DoesNotExist:
            raise Exception("Series not found")

        if title is not None:
            series.title = title
        if blogs_id is not None:
            series.blogs = Blog.objects.filter(pk__in=blogs_id)

        series.save()
        return UpdateSeries(series=series)


class DeleteSeries(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, _, id):
        try:
            series = Series.objects.get(pk=id)
        except Series.DoesNotExist:
            raise Exception("Series not found")

        series.delete()
        return DeleteSeries(success=True)


class Query(graphene.ObjectType):
    seriess = graphene.List(SeriesType)

    def resolve_seriess(self, _):
        return Series.objects.all()


class Mutation(graphene.ObjectType):
    create_series = CreateSeries.Field()
    update_series = UpdateSeries.Field()
    delete_series = DeleteSeries.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)