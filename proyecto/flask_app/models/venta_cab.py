from ..config.mysqlconnection import connectToMySQL

class Venta_cab:
    def __init__(self,data):
        self.id = data['id']
        self.fecha = data['fecha']
        self.total = data['total']
        self.usuario_id = data['usuario_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ventas_cab (fecha, total, usuario_id) VALUES (NOW, %(total)s, %(usuario_id)s);"
        return connectToMySQL('proyecto_grupal_bd').query_db(query,data)
