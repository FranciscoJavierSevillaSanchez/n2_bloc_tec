import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

#Cargar las variables de entorno
load_dotenv()

#Crear instancia
app = Flask(__name__)

#Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

#Importar modelos para que SQLAlchemy los reconozca
from app.models import Post
##from app.models import Category

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

#Importar y registrar los Blueprints
from app.routes.post import posts_bp
##from app.routes.category import categories_bp

app.register_blueprint(posts_bp, url_prefix='/posts')
##app.register_blueprint(categories_bp, url_prefix='/categories')

#Ruta principal: home
@app.route('/')
def index():
    #return 'Hola mundo'
    return render_template('index.html')