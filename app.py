from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
#no se olviden de crear la base de datos en postgres proyecto1

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:(contraseñaqui)@localhost:5432/proyecto1"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id= db.Column(db.Integer,primary_key=False)
    nombre=db.Column(db.String(50),nullable=False)
    apellidos=db.Column(db.String(60),nullable=False)
    usuario=db.Column(db.String(70),nullable=False)
    contrasenia=db.Column(db.String(40),nullable=False)  
    email=db.Column(db.String(100),nullable=False)
    #fecha=db.Column(db.) FALTA CHEQUEAR COMO ES EL DATO DE FECHA 
    admin=db.Column(db.Boolean,nullable=False)
    
    def __repr__(self):
        return f'<Todo: {self.id}, {self.nombre}, {self.apellidos}, {self.usuario},{self.contrasenia}, {self.email},{self.admin}>'



#FALTA RELLENAR
#class Tarjeta_de_cretido(db.Model):
#    __tablename__="tarjeta_de_credito"





class Equipos(db.Model):
    __tablename__="equipos"
    id= db.Column(db.Integer,primary_key=True)
    pais=db.Column(db.String(50),nullable=False)
    partidos_ganados=db.Column(db.Integer,nullable=False) 

    def __repr__(self):
        return f'<Todo: {self.id},{self.pais},{self.partidos_ganados}>'
    
class Partidos(db.Model):
    __tablename__="partidos"
    id= db.Column(db.Integer,primary_key=True)
    multiplicador_equipo_a=db.Column(db.Float,nullable=False)
    multiplicador_equipo_b=db.Column(db.Float,nullable=False)
    pais_equipo_a=db.Column(db.Integer,db.ForeignKey("equipos.id"),nullable=False)
    pais_equipo_b=db.Column(db.Integer,db.ForeignKey("equipos.id"),nullable=False)
    dinero_apostado_equipo_a=db.Column(db.Float,nullable=False)
    dinero_apostado_equipo_b=db.Column(db.Float,nullable=False)

    

    def __repr__(self):

        return f'<Todo: {self.id},{self.multiplicador_equipo_a},{self.multiplicador_equipo_b},{self.pais_equipo_a},{self.pais_equipo_b},{self.dinero_apostado_equipo_a},{self.dinero_apostado_equipo_b}>'



db.create_all()


@app.route('/')
def index():
    
    return "a"

if __name__ == '__main__':
    app.run(port=5002, debug=True)
else: 
    print('using global variables from FLASK')
