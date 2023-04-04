from .apis import book
from flask_restx import fields
from enum import Enum

class EnumDistrict(Enum):
    A = 'A'
    B = "B"
    C = "C"
    D = "D"


book_input_model = book.model('BookInputModel', {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='dd/mm/yyyy'),
    'release': fields.Raw()
})

book_output_model= book.model('BookOutputModel', {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='dd/mm/yyyy'),
    'district': fields.String(description='String type', enum=EnumDistrict._member_names_),
})

author_input_model = book.model('AuthorInputModel', {
    'name': fields.String(required=True),
    'dob': fields.DateTime(dt_format='dd/mm/yyyy'),
})

author_output_model= book.model('AuthorOutputModel', {
    'name': fields.String(required=True),
    'dob': fields.DateTime(dt_format='dd/mm/yyyy', required=True),
    'books_published': fields.List(fields.Nested(book_output_model)),
})
