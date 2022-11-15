from flask import Flask, jsonify, request
from Models import db, Productos
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:/Malena/Informatica/Planeta-Mascotas/App/database/productos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@cross_origin()
@app.route("/productos", methods=["GET"])
def getProduct():
    productos = Productos.query.all()
    toReturn = [producto.serialize() for producto in productos]
    return jsonify(toReturn), 200


@cross_origin()
@app.route("/productos/<nombre>", methods=["GET"])
def getProductByName(nombre):
    productos = db.session.query(Productos).filter(Productos.nombre.startswith(nombre))
    if not productos:
        return jsonify({"mensaje": "Este producto no existe"}), 404
    else:
        response = [producto.serialize() for producto in productos]
        return jsonify(response), 200


@cross_origin()
@app.route('/productos/<id>', methods=['DELETE'])
def eliminarProducto(id):
    producto = db.session.query(Productos).filter(Productos.id == id).first()
    db.session.delete(producto)
    db.session.commit()
    return "producto eliminado"


@cross_origin()
@app.route('/productos', methods=['POST'])
def nuevoProducto():
    request_body = request.get_json()
    producto = Productos(
        nombre=request_body.get('nombre'),
        cantidad=request_body.get('cantidad'),
        precio=request_body.get('precio'),
        imagen=request_body.get('imagen')
    )
    db.session.add(producto)
    db.session.commit()
    return jsonify(producto.serialize())


if __name__ == '__main__':
    app.run(debug=True, port=5000)
