from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
#no se olviden de crear la base de datos en postgres proyecto1

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:1234@localhost:5432/proyecto1"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_persona= db.Column(db.Integer,primary_key=False)
    nombre=db.Column(db.String(50),nullable=False)
    apellidos=db.Column(db.String(60),nullable=False)
    usuario=db.Column(db.String(70),nullable=False)
    contrasenia=db.Column(db.String(40),nullable=False)  
    email=db.Column(db.String(100),nullable=False)
    fecha_de_nacimiento=db.Column(db.Date,nullable=False) 
    ult_inicio_sesion=db.Column(db.DateTime,nullable=False)    
    rol=db.Column(db.Integer,db.ForeignKey("tipo_de_rol.id_rol"),nullable=False)
    
    def __repr__(self):
        return f'<Usuario: {self.id_persona}, {self.nombre}, {self.apellidos}, {self.usuario},{self.contrasenia}, {self.email},{self.rol}>'




class Tarjeta(db.Model):
    _tablename_ = 'tarjeta_de_credito'
    id_tarjeta = db.Column(db.Integer,primary_key =True)
    n_tarjeta = db.Column(db.Integer,nullable=False)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id_persona'),nulable=False)
    def __repr__(self):
        return f'<Tarjeta: {self.id_tarjeta},{self.n_tarjeta},{self.id_usuario}'


class Equipos(db.Model):
    __tablename__="equipos"
    id_equipo= db.Column(db.Integer,primary_key=True)
    pais=db.Column(db.String(50),nullable=False)
    n_victorias=db.Column(db.Integer,nullable=False) 
    n_derrotas= db.Column(db.Integer,nullable=False)
    


    def __repr__(self):
        return f'<Todo: {self.id},{self.pais},{self.partidos_ganados}>'
    
class Partidos(db.Model):
    __tablename__="partidos"
    id_partido= db.Column(db.Integer,primary_key=True) 
    equipo_a=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"),nullable=False)
    equipo_b=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"),nullable=False)   
      

    def __repr__(self):
        return f'<Todo: {self.id},{self.multiplicador_equipo_a},{self.multiplicador_equipo_b},{self.pais_equipo_a},{self.pais_equipo_b},{self.dinero_apostado_equipo_a},{self.dinero_apostado_equipo_b}>'


class apuestas(db.Model):
    __tablename__="apuestas"
    id_apuesta=db.Column(db.Integer,primary_key=True)
    id_partido=db.Column(db.Integer,db.ForeignKey("partidos.id_partido"))
    apuesta_a_equipo_A=db.Column(db.Boolean,nullable=False)
    apuesta_a_equipo_B=db.Column(db.Boolean,nullable=False)
    monto=db.Column(db.Integer,nullable=False)
    id_usuario=db

db.create_all()


@app.route('/')
def index():
    
    return "a"

if __name__ == '__main__':
    app.run(port=5002, debug=True)
else: 
    print('using global variables from FLASK')
