from app import db
from sqlalchemy import ForeignKey


class Pais(db.Model):
    __tablename__ = 'pais'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.nombre

class Provincia(db.Model):
    __tablename__ = 'provincia'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(
        db.Integer,
        ForeignKey('pais.id'),
        nullable=False
    )
    # Para que seoa de que tabla tomar la clave foranea.
    pais_obj = db.relationship("Pais")  
    

    def __str__(self):
        return self.nombre
    
class Localidad(db.Model):
    __tablename__ = 'localidad'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia = db.Column(
        db.Integer,
        ForeignKey('provincia.id'),
        nullable=False
    )
    provincia_obj = db.relationship("Provincia")  

    def __str__(self):
        return self.nombre
    
