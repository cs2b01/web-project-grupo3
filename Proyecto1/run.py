from flask import Flask,render_template, request, session, Response, redirect
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug = True ,port=8080, threaded=True, host=('127.0.0.1'))
