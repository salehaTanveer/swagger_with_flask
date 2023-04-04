from flask import Flask
from flask_restx import Api



def create_app():
    app = Flask(__name__)

    api = Api(app,
              title='Swagger with flask',
              version='1.0',
              description='A test project with flask-restx.'
              )

    from .api.v1.routes.initial_routes import book as book_namespace
    api.add_namespace(book_namespace)

    @app.route('/')
    def index():
        return "Swagger with flask"

    return app
