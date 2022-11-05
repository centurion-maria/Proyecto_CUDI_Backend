from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    imagen = db.Column(db.String(100))

    def __init__(self, id, nombre, cantidad, precio, imagen):
        super().__init__()
        self.id = id
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