from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:1234@192.168.1.18:5432/postgres"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Todo: {self.id}, {self.description}>'

db.create_all()


@app.route('/')
def index():
    
    return render_template('index.html', data=Todo.query.all())

if __name__ == '__main__':
    app.run(port=5002, debug=True)
else: 
    print('using global variables from FLASK')
