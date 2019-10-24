from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello

# Create api entry points
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
