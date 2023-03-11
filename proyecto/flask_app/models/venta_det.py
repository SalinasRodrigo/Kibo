from ..config.mysqlconnection import connectToMySQL

class Venta_det:
    def __init__(self,data):
        self.id = data['id']
        self.cantidad = data['cantidad']
        self.cantidad = data['subtotal']
        self.producto_id = data['producto_id']
        self.venta_cab = data['venta_cab']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO ventas_det (cantidad, subtotal, producto_id, venta_cab)
          VALUES (%(cantidad)s, %(subtotal)s, %(producto_id)s, %(venta_cab)s);"""
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)
