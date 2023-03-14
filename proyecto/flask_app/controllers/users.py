from flask_app import app
from flask import render_template, request, redirect, session, flash
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto
from flask_bcrypt import Bcrypt
from ..models.user import User

bcrypt = Bcrypt(app)

app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedido')
def pedido():
    return render_template('finalizar_pedido.html')

@app.route('/buscador')
def buscador():
    return render_template('buscador.html')

@app.route('/registrar', methods=['POST', 'GET'])
def registro():
    if request.method=='POST':
        if request.form['contraseña'] == request.form['confi']:
            if User.validar_usuario(request.form):
                pw_hash = bcrypt.generate_password_hash(request.form['contraseña'])
                data = {
                    'nombre' : request.form['nombre'],
                    'apellido' : request.form['apellido'],
                    'correo' : request.form['correo'],
                    'password' : pw_hash,
                    'direccion' : request.form['direccion'],
                    'celular' : request.form['celular']
                }
                usuario = User.save(data)
                flash("Registro Exitoso!!!")
                return redirect('/')
            else:
                return redirect('/')
        else:
            flash("Las Contraseñas no Coinciden!!!")
            return redirect('/')
    else:
        return redirect('/')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        # ver si el correo de usuario proporcionado existe en la base de datos
        data = {
            "correo" : request.form.get("correo")
        }
        user_in_db = User.getbyEmail(data)

        # usuario no está registrado en la base de datos
        if not user_in_db:
            flash("Email no registrado")
            return redirect('/')
        
        if not bcrypt.check_password_hash(user_in_db.password, request.form['contraseña']):
            # si obtenemos False después de verificar la contraseña
            flash("Password incorrecto")
            return redirect('/')
        
        # si las contraseñas coinciden, configuramos el user_id en sesión
        session['user_id'] = user_in_db.id
        if user_in_db.nivel == 1:
            return redirect('/dashboard')
        else:
            return redirect('/')
    
    else:
        return redirect('/')
    

@app.route('/dashboard')
def dashboard():
    return render_template('/dashboard/dashboard.html')

@app.route('/dashboard/productos')
def producto_add():
    return render_template('/dashboard/productos.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/dashboard/logout')
def logout():
    session.clear()
    return redirect('/')
