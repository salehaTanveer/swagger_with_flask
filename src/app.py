from flask import Flask
from flask_restx import Api



def create_app():
    app = Flask(__name__)

    api = Api(app,
              title='Swagger with flask',
              version='1.0',
              description='A test project with flask-restx.'
              )

    from .api.v1.routes.initial_routes import hello_world
    api.add_namespace(hello_world)

    @app.route('/')
    def index():
        return "Swagger with flask"

    return app
