from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:Softjuandius_25@localhost:5432/proyecto1"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id= db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50),nullable=True)
    apellidos=db.Column(db.String(60),nullable=True)
    usuario=db.Column(db.String(70),nullable=True)
    contrasenia=db.Column(db.String(40),nullable=True)  
    email=db.Column(db.String(100),nullable=True)
'''
class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'
    id = db.Column(db.Integer,primary_key =True)
    n_tarjeta = db.Column(db.Integer,nullable=False)
    id_usuario = db.Column(db.Integer,db.ForeignKey('Usuario.id'))
'''
db.create_all()


@app.route('/')
def index():
    
    return "a"

if __name__ == '__main__':
    app.run(port=5002, debug=True)
else: 
    print('using global variables from FLASK')
