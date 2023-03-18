from flask_app import app
from flask import render_template, request, redirect, session, flash, jsonify
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto
from ..models.user import User

@app.route('/dashboard/productos')
def producto():
    return render_template('/dashboard/productos.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

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
                return jsonify(mensaje = "Imagen no válida, las extensiones permitidas son .png, .jpg, .jpeg")

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
        return redirect('/dashboard/productos')
    else:
        return redirect('/dashboard/productos')

@app.route('/process_categoria', methods=['POST'])
def registrar_categoria():
    if request.method == 'POST':
        data = {
            "nombre":request.form['nombre'],
        }
        Categoria.save(data)
        return redirect('/dashboard/productos')
    else:
        return redirect('/dashboard/productos')
    
@app.route('/process_marca', methods=['POST'])
def registrar_marca():
    if request.method == 'POST':
        data = {
            "nombre":request.form['nombre'],
        }
        Marca.save(data)
        return redirect('/dashboard/productos')
    else:
        return redirect('/dashboard/productos')
    
@app.route('/dashboard/modificar_producto')
def actualizar_producto():
    return render_template('/dashboard/actualizar_producto.html', marcas = Marca.get_all(), categorias = Categoria.get_all(), productos = Producto.get_all())

@app.route('/reponer_stock/<int:id>')
def reponer_stock(id):
    Producto.update_stock(id)
    return redirect("/dashboard/modificar_producto")


@app.route('/obtener_producto/<int:id>')
def obtener_producto(id):
    producto = Producto.get_one(id)
    return jsonify(producto)

@app.route('/process_actualizar_producto', methods=['POST'])
def proceso_actualizar_producto():
    if request.method == 'POST':
        path_database = None
        data = {}
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
                return ("/dashboard/productos")

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
        else:
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
        return redirect('/dashboard/modificar_producto')
    else:
        return redirect('/dashboard/modificar_producto')

@app.route('/producto_seleccionado/<int:id>')
def producto_seleccinado(id):
    producto = Producto.get_one(id)
    if producto != None:
        return render_template('producto_seleccionado.html', producto = producto, funciones = Producto)
    else:
        return redirect("/")


@app.route('/carrito_add', methods=['POST'])
def agregar_carrito():
    listaNueva = []
    if request.method == 'POST':
        id = request.form.get("id")
        if "user_id" in session:
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
            flash("Inicia sesión para poder agregar productos")
            return redirect('/producto_seleccionado/'+id)
    else:
        return redirect('/')
    
@app.route('/carrito_delete/<int:id>')
def eliminar_carrito(id):
    if "user_id" in session:
        listaNueva = session["carrito"].copy()
        for idx, articulo in enumerate(session["carrito"]):
            if id == int(articulo[0]):
                session["carrito"].pop(idx)
                listaNueva = session["carrito"].copy()
                break
        session["carrito"] = listaNueva
        return redirect('/carrito')
    else:
        return redirect('/carrito')
    

@app.route('/carrito')
def mostrar_carrito():
    if "user_id" in session:
        if "carrito" in session and len(session["carrito"]) > 0:
            ids = []
            for producto in session["carrito"]:
                ids.append(producto[0]) 
            data_usuario = {
                "id" : session["user_id"]
            }
            return render_template("finalizar_pedido.html", productos = Producto.get_carrito(ids), usuario = User.getUserId(data_usuario))
        else:
            flash("No tienes elementos agregados")
            return redirect("/")
    else:
        flash("Inicia sesión para poder acceder al carrito")
        return redirect("/")