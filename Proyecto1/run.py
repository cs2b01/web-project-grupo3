from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
from datetime import datetime

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/static/<content>', methods=['GET','POST','PUT','DELETE'])
def static_content(content):
    return render_template(content)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/ubicanos')
def ubicanos():
    return render_template('ubicanos.html')


@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')


@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/users', methods = ['GET'])
def get_users():
    session = db.getSession(engine)
    dbResponse = session.query(entities.User)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route('/users', methods = ['POST'])
def create_user():
    c =  json.loads(request.form['values'])
    user = entities.User(
        username=c['username'],
        name=c['name'],
        fullname=c['fullname'],
        password=c['password']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    return 'Created User'


@app.route('/users', methods = ['PUT'])
def update_user():
    session = db.getSession(engine)
    id = request.form['key']
    user = session.query(entities.User).filter(entities.User.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(user, key, c[key])
    session.add(user)
    session.commit()
    return 'Updated User'


@app.route('/users', methods = ['DELETE'])
def delete_user():
    id = request.form['key']
    session = db.getSession(engine)
    users = session.query(entities.User).filter(entities.User.id == id).one()
    session.delete(users)
    session.commit()
    return "Deleted User"


@app.route('/users/<id>', methods = ['GET'])
def get_user(id):
    db_session = db.getSession(engine)
    users = db_session.query(entities.User).filter(entities.User.id == id)
    for user in users:
        js = json.dumps(user, cls=connector.AlchemyEncoder)
        return  Response(js, status=200, mimetype='application/json')

    message = { 'status': 404, 'message': 'Not Found'}
    return Response(message, status=404, mimetype='application/json')


@app.route('/compras', methods = ['GET'])
def get_compra():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Compras)
    data = []
    for compra in dbResponse:
        data.append(compra)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route('/compras', methods = ['POST'])
def create_compra():
    c =  json.loads(request.form['values'])
    compra = entities.Compras(
        usercomprador_id=c['usercomprador']['username']['id'],
        producto_id=c['producto']['nombre']['id'],
        satisfaccion=c['satisfaccion']
    )
    session = db.getSession(engine)
    session.add(compra)
    session.commit()
    return 'Created Compra'


@app.route('/compras', methods = ['PUT'])
def update_compra():
    session = db.getSession(engine)
    id = request.form['key']
    compra = session.query(entities.Compras).filter(entities.Compras.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(compra, key, c[key])
    session.add(compra)
    session.commit()
    return 'Updated User'


@app.route('/compras', methods = ['DELETE'])
def delete_compra():
    id = request.form['key']
    session = db.getSession(engine)
    compras = session.query(entities.Compras).filter(entities.Compras.id == id).one()
    session.delete(compras)
    session.commit()
    return "Deleted Compras"


@app.route('/productos', methods = ['GET'])
def get_productos():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Producto)
    data = []
    for producto in dbResponse:
        data.append(producto)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route('/productos', methods = ['POST'])
def create_productos():
    c =  json.loads(request.form['values'])
    producto = entities.Producto(
        codigo=c['codigo'],
        nombre=c['nombre'],
        marca=c['marca'],
        caracteristicas=c['caracteristicas'],
        cantidad=c['cantidad'],
        precio=c['precio'],
        imagen=c['imagen']
    )
    session = db.getSession(engine)
    session.add(producto)
    session.commit()
    return 'Created producto'


@app.route('/productos', methods = ['PUT'])
def update_producto():
    session = db.getSession(engine)
    id = request.form['key']
    producto = session.query(entities.Producto).filter(entities.Producto.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(compra, key, c[key])
    session.add(compra)
    session.commit()
    return 'Updated User'


@app.route('/productos', methods = ['DELETE'])
def delete_producto():
    id = request.form['key']
    session = db.getSession(engine)
    productos = session.query(entities.Producto).filter(entities.Producto.id == id).one()
    session.delete(productos)
    session.commit()
    return "Deleted Compras"


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug = True ,port=8080, threaded=True, host=('127.0.0.1'))

