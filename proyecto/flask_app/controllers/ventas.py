from flask_app import app
from flask import render_template, request, redirect, session, flash, jsonify
from ..models.categoria import Categoria
from ..models.marca import Marca
from ..models.producto import Producto

@app.route('/pago_exitoso/')
def procesar_venta():
    print("Gracias por comprar con nosotros")
    return render_template('index.html')


@app.route('/pago_cancelado/')
def pago_cancelado():
    print("Bajón cancelaste")
    return render_template('index.html')