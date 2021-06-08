from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:1234@192.168.1.18:5432/postgres"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario:
    id= db.Column(db.integer,primary_key=True)


db.create_all()


@app.route('/')
def index():
    
    return "a"

if __name__ == '__main__':
    app.run(port=5002, debug=True)
else: 
    print('using global variables from FLASK')
