from .apis import hello_world
from flask_restx import fields
from enum import Enum

class EnumDistrict(Enum):
    A = 'A'
    B = "B"
    C = "C"
    D = "D"

input_model = hello_world.model('InputModel', {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
})

output_model= hello_world.model('OutputModel', {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
    'district': fields.String(description='String type', enum=EnumDistrict._member_names_),
})