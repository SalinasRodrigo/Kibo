from flask_app import app
from flask import render_template, request, redirect, session, flash, jsonify
from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto
from ..models.venta_cab import Venta_cab
from ..models.venta_det import Venta_det

@app.route('/pago_exitoso/')
def procesar_venta():
    datos_venta_cab = {
        "usuario_id" : session["user_id"]
    }
    Venta_cab.save(datos_venta_cab)
    ids = []
    for producto_id in session["carrito"]:
        ids.append(producto_id[0])
    for idx in range(len(session["carrito"])):
        datos_venta_det = {
            "cantidad" : session["carrito"][idx][1],
            "subtotal" : Producto.obtener_precio(session["carrito"][idx][0]) * session["carrito"][idx][1],
            "producto_id" : session["carrito"][idx][0],
            "venta_cab_id" : Venta_cab.obtener_id_venta(),
        }
        Venta_det.save(datos_venta_det)
        datos_producto = {
            "id" : session["carrito"][idx][0],
            "cantidad" : session["carrito"][idx][1]
        }
        Producto.update_venta(datos_producto)
    datos_update = {
        "total" : Venta_det.obtener_total(Venta_cab.obtener_id_venta()),
        "id" : Venta_cab.obtener_id_venta()
    }
    Venta_cab.update(datos_update)
    session.pop('nuevo')
    session.pop('carrito')
    flash("Su pago fue procesado exitosamente.")
    return redirect("/")


@app.route('/pago_cancelado/')
def pago_cancelado():
    flash("Pago cancelado.")
    return redirect("/")