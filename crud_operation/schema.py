import graphene
from graphene_django import DjangoObjectType

from .models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        fields = '__all__'


class BookCreation(graphene.Mutation):
    response = graphene.String()
    success_code = graphene.String()
    error_code = graphene.String()

    class Argument:
        pass

    @classmethod
    def mutate(cls, root, info, **kwargs):
        print(kwargs)
        return BookCreation(respone="Success", success_code="201")


class AuthorCreation(graphene.Mutation):
    response = graphene.String()
    success_code = graphene.String()
    error_code = graphene.String()

    class Argument:
        user_name = graphene.String(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        email = graphene.String(required=True)
        phone_number = graphene.String(required=True)

    @classmethod
    def mutate(cls,root,info,**kwargs):
        print(kwargs)
        return AuthorCreation(respone="Success", success_code="201")


