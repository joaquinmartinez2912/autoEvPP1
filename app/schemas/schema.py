from app import ma
from marshmallow import fields

class PaisSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    nombre = fields.String()
    
class ProvinciaSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    nombre = fields.String()
    pais = fields.Integer()
    pais_obj = fields.Nested(PaisSchema, exclude=("id",))

class LocalidadSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    nombre = fields.String()
    provincia = fields.Integer()
    provincia_obj = fields.Nested(ProvinciaSchema, exclude=("id","pais"))

