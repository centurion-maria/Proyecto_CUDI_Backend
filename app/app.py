from flask import Flask, jsonify, request
from Models import db, Productos
from logging import exception
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
    try:
        productos = Productos.query.all()
        toReturn = [producto.serialize() for producto in productos]
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500


@cross_origin()
@app.route("/productos/<nombre>", methods=["GET"])
def getProductByName():
    try:
        marcaProducto = request.args["name"]
        producto = Productos.query.filter_by(name=marcaProducto).first()
        if not producto:
            return jsonify({"msg": "Este producto no existe"}), 200
        else:
            return jsonify(producto.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
