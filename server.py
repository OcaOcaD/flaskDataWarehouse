from flask import Flask, render_template, request
from flask.wrappers import Request

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hola mundo</p>"

@app.route('/registra')
def registra():
    return render_template('registra.html')

@app.route('/procesa', methods=['POST'])
def procesa():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    carrera = request.form['carrera']
    return "<h1>Datos recibidos</h1>"+ "<p>" + nombre + "</p>" + "<p>" + codigo + "</p>" + "<p>" + carrera + "</p>"
if __name__ == '__main__':
    app.run()