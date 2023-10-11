from app import app, db

from flask import jsonify, request

# Imports de variables generadas por nosotros
from app.models.models import (
    Localidad,
    Pais,
    Provincia,
)
from app.schemas.schema import (
    PaisSchema,
    ProvinciaSchema,
    LocalidadSchema
)

from flask.views import MethodView

@app.route('/')
def index():
    return "<h1> Hola Flask </h1>"

class PaisAPI(MethodView):
    def get(self, pais_id=None):
        if pais_id is None:
            paises = Pais.query.all()
            resultado = PaisSchema().dump(paises, many=True)
        else:
            pais = Pais.query.get(pais_id)
            resultado = PaisSchema().dump(pais)
        return jsonify(resultado)
    
    def post(self):
        pais_json = request.get_json()
        pais_json = PaisSchema().load(request.json)
        nombre = pais_json.get("nombre")

        nuevo_pais = Pais(nombre=nombre)
        db.session.add(nuevo_pais)
        db.session.commit()
        return jsonify(Mensaje=f"Se agrego el pais {nombre}")


app.add_url_rule("/pais", view_func=PaisAPI.as_view("pais"))

app.add_url_rule("/pais/<pais_id>",view_func=PaisAPI.as_view("pais_por_id"))


class ProvinciaAPI(MethodView):
    
    def post(self):
        provincia_json = request.get_json()
        provincia_json = ProvinciaSchema().load(request.json)
        nombre = provincia_json.get("nombre")
        pais = provincia_json.get("pais")

        nueva_provincia = Provincia(nombre=nombre, pais=pais)
        db.session.add(nueva_provincia)
        db.session.commit()
        return jsonify(Mensaje=f"Se agrego la provincia {nombre}")


app.add_url_rule("/provincia", view_func=ProvinciaAPI.as_view("provincia"))

app.add_url_rule("/provincia/<provincia_id>",view_func=ProvinciaAPI.as_view("provincia_por_id"))