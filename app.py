import os
from flask import Flask, jsonify, request
from Models import db, Productos
from logging import exception
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@cross_origin()
@app.route("/productos", methods=["GET"])
def getProduct():
    try:
        productos = Productos.query.all()
        toReturn = [producto.serialize() for producto in productos]
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"mensaje": "Ha ocurrido un error"}), 500


@cross_origin()
@app.route("/productos/<nombre>", methods=["GET"])
def getProductByName(nombre):
    try:
        productos = db.session.query(Productos).filter(Productos.nombre.startswith(nombre))
        if not productos:
            return jsonify({"mensaje": "Este producto no existe"}), 200
        else:
            response = [producto.serialize() for producto in productos]
            return jsonify(response), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"mensaje": "Ha ocurrido un error"}), 500


@app.route('/productos/eliminar/<id>', methods=['DELETE'])
def eliminarProducto(id):
        producto = db.session.query(Productos).filter(Productos.id == id).first()
        db.session.delete(producto)
        db.session.commit()
        return "producto eliminado"


@app.route('/productos', methods=['POST'])
def nuevoProducto():
    nuevoProducto = Productos(
        nombre=request.form.get('nombre'),
        cantidad=request.form.get('cantidad'),
        precio=request.form.get('precio'),
        imagen=request.form.get('imagen')
    )
    db.session.add(nuevoProducto)
    db.session.commit()
    return jsonify(nuevoProducto.serialize())


if __name__ == '__main__':
    app.run(debug=True, port=5000)
