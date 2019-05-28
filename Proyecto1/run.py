from flask import Flask,render_template, request, session, Response, redirect
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/ubicanos')
def ubicanos():
    return render_template('ubicanos.html')


@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug = True ,port=8080, threaded=True, host=('127.0.0.1'))