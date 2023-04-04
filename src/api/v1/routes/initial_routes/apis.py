from flask import Flask, request, Blueprint
from flask_restx import Resource, fields, Namespace
# from . import hello_world

hello_world_example = {'message': 'Hello World!'}
book = Namespace("book")


from .schemas import *


@book.route('/author/')
class AuthorView(Resource):
    """
    Short view description for HelloWorld
    """
    @book.marshal_list_with(author_output_model, mask='token', code=200)
    # @hello_world.response(500, 'Internal Server error')
    def get(self):
        """
        Get books author endpoint
        """
        return hello_world_example

    @book.marshal_list_with(author_input_model, code=200)
    def post(self):
        """
        Add books author post endpoint
        :return:
        """
        pass


@book.route('/')
class BookView(Resource):
    """
    Short view description for HelloWorld
    """
    @book.marshal_list_with(book_input_model, code=200)
    # @hello_world.response(500, 'Internal Server error')
    def get(self):
        """
        Get book endpoint
        """
        return hello_world_example

    @book.marshal_list_with(book_output_model, code=200)
    def post(self):
        """
        Add book post endpoint
        :return:
        """
        pass