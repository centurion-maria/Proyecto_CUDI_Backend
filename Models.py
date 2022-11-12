from flask_sqlalchemy import *

db = SQLAlchemy()


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre, cantidad, precio, imagen):
        super().__init__()
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.imagen = imagen

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio,
            "imagen": self.imagen
        }