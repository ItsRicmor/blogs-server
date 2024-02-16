import graphene

from author_app import schema as author_schema
from blog_app import schema as blog_schema
from series_app import schema as series_schema


class Query(author_schema.Query, blog_schema.Query, series_schema.Query, graphene.ObjectType):
    # Combine the queries from different apps
    pass


class Mutation(author_schema.Mutation, blog_schema.schema.Mutation, series_schema.Mutation, graphene.ObjectType):
    # Combine the mutations from different apps
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)