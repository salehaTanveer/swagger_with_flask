from flask import Flask, request, Blueprint
from flask_restx import Resource, fields, Namespace
# from . import hello_world

hello_world_example = {'message': 'Hello World!'}
hello_world = Namespace("step")


from .schemas import input_model, output_model


@hello_world.route('/')
class HelloWorld(Resource):
    """
    Short view description for HelloWorld
    """
    @hello_world.marshal_list_with(input_model, code=200)
    # @hello_world.response(500, 'Internal Server error')
    def get(self):
        """
        Hello world message endpoint
        """
        return hello_world_example

    @hello_world.marshal_list_with(output_model, code=200)
    def post(self):
        """
        Hello world post endpoint
        :return:
        """
        pass
