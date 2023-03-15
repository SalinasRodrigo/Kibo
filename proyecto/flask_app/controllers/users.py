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
    productos = Producto.get_all()
    return render_template('index.html', productos = productos)

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
            return redirect('/')#, user = session["user_id"])

    else:
        return redirect('/')
    

@app.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect('/')
    else:
        data ={
            "id" : session['user_id']
        }    
        user_in_db = User.getDataUser(data)
        if user_in_db.nivel == 1:
            return render_template('/dashboard/dashboard.html')
        else:
            return redirect('/')
        

@app.route('/dashboard/productos')
def producto_add():
    return render_template('/dashboard/productos.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/dashboard/perfil')
def perfil():
    data = {
        "id" : session['user_id']
    }
    user = User.getDataUser(data)
    return render_template('/dashboard/perfil.html', user=user)

@app.route('/dashboard/user/<int:id>', methods=['POST','GET'])
def update_user(id):
    if request.method == 'POST':
        datos ={
            'id': id,
            'nombre' : request.form['nombre'],
            'apellido' : request.form['apellido'],
            'celular' : request.form['celular'],
            'direccion' : request.form['direccion'],
            'correo' : request.form['correo']
        }
    
    User.update(datos)
    flash("Datos Actualizados!!!")
    return redirect('/dashboard')


@app.route('/dashboard/change_password', methods=['POST','GET'])
def chg_pass():
    if request.method=='POST':

        if request.form['contraseña'] == request.form['confi']:

            pw_hash = bcrypt.generate_password_hash(request.form['contraseña'])

            data = {
                "id" : session['user_id'],
                "contraseña" : pw_hash,
                "confi" : request.form['confi']
            }
            User.ChangePassword(data)
            flash("Contraseña Cambiada")
            return redirect('/dashboard')

        else:
            flash('Atención. Las contraseñas no coinciden!!!')
            render_template('/dashboard/change_pass.html')
    
    return render_template('/dashboard/change_pass.html')

@app.route('/dashboard/logout')
def logout():
    session.clear()
    return redirect('/')
