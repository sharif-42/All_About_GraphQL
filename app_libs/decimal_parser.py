from graphene import Scalar
from graphene.types import decimal
from graphql.language import ast


class Decimal(Scalar):
    """
    this section is for parsing decimal data
    The Decimal scalar type represents a python Decimal.
    """

    @staticmethod
    def serialize(dec):
        assert isinstance(dec, decimal.Decimal), (
            'Received not compatible Decimal "{}"'.format(repr(dec))
        )
        return str(dec)

    @staticmethod
    def parse_value(value):
        return decimal.Decimal(value)

    @classmethod
    def parse_literal(cls, node):
        if isinstance(node, ast.StringValue):
            return cls.parse_value(node.value)
