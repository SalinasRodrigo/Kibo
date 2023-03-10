from flask_app import app
from flask import render_template, request, redirect, session, flash
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto

@app.route('/producto')
def producto():
    return render_template('producto.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/process_producto', methods=['POST'])
def registrar_producto():
    if request.method == 'POST':
        path_database = None
        if request.files["imagen"].filename != "":
            EXTENSIONES_PERMITIDAS = set([".png", ".jpg", ".jpeg"])
            file     = request.files['imagen']
            basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
            direccion = Path(basepath)

            filename = secure_filename(file.filename) #Nombre original del archivo
            
            #capturando extension del archivo ejemplo: (.png, .jpg)
            extension = os.path.splitext(filename)[1]
            #validando la extension
            if not extension in EXTENSIONES_PERMITIDAS:
                flash("Imagen no válida, las extensiones permitidas son .png, .jpg, .jpeg")
                return ("/producto")

            nuevoNombreFile     = str(Producto.obtener_id_siguiente()) + extension
            #direccion.parents[0] retrocede una carpeta
            upload_path = os.path.join (direccion.parents[0], 'static/files', nuevoNombreFile) 
            file.save(upload_path)
            path_database = f"/static/files/{nuevoNombreFile}"

        data = {
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "precio": request.form["precio"],
            "imagen": path_database,
            "stock_ideal": request.form["stock_ideal"],
            "stock_disponible": request.form["stock_disponible"],
            "marca_id": request.form["marca"],
            "categoria_id": request.form["categoria"]
        }
        Producto.save(data)
        return redirect('/producto')
    else:
        return redirect('/producto')

@app.route('/process_categoria', methods=['POST'])
def registrar_categoria():
    if request.method == 'POST':
        data = {
            "nombre":request.form['nombre'],
        }
        Categoria.save(data)
        return redirect('/producto')
    else:
        return redirect('/producto')
    
@app.route('/process_marca', methods=['POST'])
def registrar_marca():
    if request.method == 'POST':
        data = {
            "nombre":request.form['nombre'],
        }
        Marca.save(data)
        return redirect('/producto')
    else:
        return redirect('/producto')
    
@app.route('/actualizar_producto')
def actualizar_producto():
    return render_template('actualizar_producto.html', productos = Producto.get_all())

@app.route('/process_actualizar_producto', methods=['POST'])
def proceso_actualizar_producto():
    if request.method == 'POST':
        data = {
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "precio": request.form["precio"],
            "imagen": path_database,
            "stock_ideal": request.form["stock_ideal"],
            "stock_disponible": request.form["stock_disponible"],
            "descuento": request.form["descuento"],
            "marca_id": request.form["marca"],
            "categoria_id": request.form["categoria"]
        }
        Producto.update_producto(data)
        return redirect('/actualizar_producto')
    else:
        return redirect('/actualizar_producto')
