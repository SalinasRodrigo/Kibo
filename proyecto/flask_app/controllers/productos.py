from flask_app import app
from flask import render_template, request, redirect, session, flash, jsonify
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
    
@app.route('/modificar_producto')
def actualizar_producto():
    return render_template('actualizar_producto.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/reponer_stock/<int:id>')
def reponer_stock(id):
    Producto.update_stock(id)
    return redirect("/modificar_producto")


@app.route('/obtener_producto/<int:id>')
def obtener_producto(id):
    producto = Producto.get_one(id)
    return jsonify(producto)

@app.route('/process_actualizar_producto', methods=['POST'])
def proceso_actualizar_producto():
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

            nuevoNombreFile     = str(request.form["id"]) + extension
            #direccion.parents[0] retrocede una carpeta
            upload_path = os.path.join (direccion.parents[0], 'static/files', nuevoNombreFile) 
            file.save(upload_path)
            path_database = f"/static/files/{nuevoNombreFile}"
            data = {
                "id": request.form["id"],
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
        data = {
            "id": request.form["id"],
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "precio": request.form["precio"],
            "stock_ideal": request.form["stock_ideal"],
            "stock_disponible": request.form["stock_disponible"],
            "descuento": request.form["descuento"],
            "marca_id": request.form["marca"],
            "categoria_id": request.form["categoria"]
        }
        Producto.update_producto(data)
        return redirect('/modificar_producto')
    else:
        return redirect('/modificar_producto')

@app.route('/producto_seleccionado/<int:id>')
def producto_seleccinado(id):
    return render_template('producto_seleccionado.html', producto = Producto.get_one(id))


@app.route('/carrito_add', methods=['POST'])
def agregar_carrito():
    listaNueva = []
    if request.method == 'POST':
        id = request.form.get("id")
        if request.form.get("cantidad") != "" and int(request.form.get("cantidad")) > 0:
            cantidad = int(request.form.get("cantidad"))
            stock = Producto.get_stock(id)
            if stock >= cantidad:
                if not "carrito" in session:
                    session["carrito"] = []
                    session["carrito"].append([id, cantidad])
                    listaNueva = session["carrito"].copy()
                else:
                    #Consula si el articulo se habia agregado previamente
                    existe = False
                    cantidad_anterior = 0
                    indice = None
                    for idx, articulo in enumerate(session["carrito"]):
                        if id == articulo[0]:
                            existe = True
                            cantidad_anterior = articulo[1]
                            indice = idx
                            break
                    #si se habia agregado previamente consulta si hay stock suficiente
                    if existe:
                        if stock >= (cantidad + cantidad_anterior):
                            #si hay stock se actualiza la cantidad
                            session["carrito"][indice][1] = cantidad + cantidad_anterior
                            listaNueva = session["carrito"].copy()
                        else:
                            flash(f"Stock Insuficiente solo quedan {stock - cantidad_anterior} en existencia")
                            return redirect('/producto_seleccionado/'+id)
                    else:
                        session["carrito"].append([id, cantidad])
                        listaNueva = session["carrito"].copy()
                session["nuevo"] = listaNueva
                return redirect('/carrito')
            else:
                flash(f"Stock Insuficiente solo quedan {stock} en existencia")
                return redirect('/producto_seleccionado/'+id)
        else:
            flash("Completa la cantidad de artículos que deseas comprar")
            return redirect('/producto_seleccionado/'+id)
    else:
        return redirect('/')
    

@app.route('/carrito')
def mostrar_carrito():
    #poner validación cuando tengamos usuarios para no permitir que entren
    if "carrito" in session:
        ids = []
        for producto in session["carrito"]:
            ids.append(producto[0]) 
        return render_template("finalizar_pedido.html", productos = Producto.get_carrito(ids))
    else:
        return render_template("finalizar_pedido.html")