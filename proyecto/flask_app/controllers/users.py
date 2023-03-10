from flask_app import app
from flask import render_template, request, redirect, session, flash
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedido')
def pedido():
    return render_template('finalizar_pedido.html')