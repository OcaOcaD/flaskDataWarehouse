from flask import Flask, render_template, request
from flask.wrappers import Request
from db import conectar, getListadoPersonas, guardaEmpleado

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hola mundo</p>"

@app.route('/register')
def register():
    return render_template('register.html')

# Handle Form
@app.route('/procesa', methods=['POST'])
def procesa():
    name = request.form['name']
    lastname = request.form['lastname']
    sex = request.form['sex']
    isMedic = request.form['isMedic']
    email = request.form['email']
    password = request.form['password']
    confirmPassword = request.form['confirmPassword']
    #insertar en base de datos
    return "<h1>Data received</h1>" + name 


@app.route('/listado')
def listado():
    conexion = conectar()
    if conexion == None:
        return '<p> Error de conexion...</p>'
    else:
        listado = getListadoPersonas(conexion)
        return render_template('listado.html', listado=listado)

@app.route('/nuevo')
def nuevo():
    return render_template("nuevo.html")

@app.route('/guardaEmpleado', methods=['POST'])
def guardaEmpleado():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    anio = request.form['anio']
    genero = request.form['genero']
    conexion = conectar()
    if guardaEmpleado(conexion,nombre,apellidos,anio,genero):
        return render_template('aviso.html')
    else:
        return "<p>Error al guardar la informacion</p>"

if __name__ == '__main__':
    app.run()