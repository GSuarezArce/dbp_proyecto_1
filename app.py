from logging import error
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import json
import datetime



app = Flask(__name__)

#no se olviden de crear la base de datos en postgres proyecto1

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://grupo5:1234@localhost:5432/proyecto1"   

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate= Migrate(app,db)


class Rol(db.Model):
    __tablename__="rol"
    id_rol=db.Column(db.Integer,primary_key=True)
    rol= db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f"<Rol: {self.id_rol}, {self.rol}>"
        


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_persona= db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50),nullable=False)
    apellidos=db.Column(db.String(60),nullable=False)
    usuario=db.Column(db.String(70),nullable=False)
    contrasenia=db.Column(db.String(40),nullable=False)  
    email=db.Column(db.String(100),nullable=False)
    fecha_de_nacimiento=db.Column(db.Date,nullable=False) 
    dinero_en_cuenta=db.Column(db.Float,nullable=False)
    ult_inicio_sesion=db.Column(db.DateTime,nullable=False)    
    rol=db.Column(db.Integer,db.ForeignKey("rol.id_rol"),nullable=False)
    
    def __repr__(self):
        return f'<Usuario: {self.id_persona}, {self.nombre}, {self.apellidos}, {self.usuario},{self.contrasenia}, {self.email},{self.rol}>'




class Tarjeta(db.Model):
    __tablename__ = 'tarjeta_de_credito'
    id_tarjeta = db.Column(db.Integer,primary_key =True)
    n_tarjeta = db.Column(db.Integer,nullable=False)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id_persona'),nullable=False)
    def __repr__(self):
        return f'<Tarjeta: {self.id_tarjeta},{self.n_tarjeta},{self.id_usuario}>'

class Solicitud(db.Model):
    __tablename__="solicitudes"
    id_solicitud=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(10000),nullable=False)
    monto_solicitado=db.Column(db.Float,nullable=False)
    id_persona=db.Column(db.Integer,db.ForeignKey('usuario.id_persona'),nullable=False)

    def __repr__(self):
        return f"<Solicitud: {self.id_solicitud}, {self.description}, {self.monto_solicitado},{self.id_persona}>"
        

class Equipos(db.Model):
    __tablename__="equipos"
    id_equipo= db.Column(db.Integer,primary_key=True)
    pais=db.Column(db.String(50),nullable=False)
    n_victorias=db.Column(db.Integer,nullable=False) 
    n_derrotas= db.Column(db.Integer,nullable=False)
    


    def __repr__(self):
        return f'<Todo: {self.id_equipo},{self.pais},{self.n_derrotas},{self.n_victorias}>'
    
class Partidos(db.Model):
    __tablename__="partidos"
    id_partido= db.Column(db.Integer,primary_key=True) 
    equipo_a=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"),nullable=False)
    equipo_b=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"),nullable=False)   
      

    def __repr__(self):
        return f'<Todo: {self.id_partido},{self.equipo_a},{self.equipo_b}>'


class apuestas(db.Model):
    __tablename__="apuestas"
    id_apuesta=db.Column(db.Integer,primary_key=True)
    id_partido=db.Column(db.Integer,db.ForeignKey("partidos.id_partido"),nullable=False)
    apuesta_a_equipo_A=db.Column(db.Boolean,nullable=False)
    apuesta_a_equipo_B=db.Column(db.Boolean,nullable=False)
    monto=db.Column(db.Integer,nullable=False)
    id_usuario=db.Column(db.Integer,db.ForeignKey("usuario.id_persona"),nullable=False)

    def __repr__(self):
        return f'<Todo: {self.id_apuesta},{self.id_partido},{self.apuesta_a_equipo_A},{self.apuesta_a_equipo_B},{self.monto},{self.id_usuario}>'



@app.route('/comprobar-credenciales',methods=['POST'])
def comprobar_credenciales():
    response={}
    usuario=request.get_json()['usuario']
    password=request.get_json()['password']
    lista_usuarios=Usuario.query.all()
    us=Usuario(id_persona=1,nombre="pepe",apellidos="nose",usuario="Ereiclo",contrasenia="1234",email="adjkf@tumama.com",fecha_de_nacimiento=datetime.date.today(),dinero_en_cuenta=1234,ult_inicio_sesion=datetime.datetime.now(),rol=1)

    lista_usuarios.append(us)
    for u in lista_usuarios:
        if usuario==u.usuario and password==u.contrasenia:
            response['resultado']="success"
            response['username']=u.usuario
            response['password']=u.contrasenia
            
        
        elif usuario==u.usuario and password!=u.contrasenia:
            response['resultado']="incorrect_password"
        else:
            response['resultado']="incorrect_username"
        
    
        

    return jsonify(response)
    

@app.route('/redirect',methods=['POST'])
def prueba():
    d =request.form
    
    
    return render_template('prueba.html',data= {"usuario" : d["usuario"], "password": d["password"]})

@app.route('/')
def index():
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5002, debug=True)
else: 
    print('using global variables from FLASK')
