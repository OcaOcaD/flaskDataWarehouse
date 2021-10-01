from flask import Flask, render_template, request
from flask.wrappers import Request
from db import conectar, getListadoPersonas, guardaEmpleado, saveEmployeeAndIsMedic,saveEmployee, getEnfermedades

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
    name = request.form['name-input']
    lastname = request.form['lastname-input']
    birthdate = request.form['birthdate-input']
    sex = request.form['sex-input']
    email = request.form['email-input']
    password = request.form['password-input']
    confirmPassword = request.form['confirmPassword-input']
    isMedic = request.form['isMedicField']
    cedula = request.form['medicIdCard-input']
    
    return "<h1>Data received</h1>" + name + isMedic + birthdate
    
    
    # conexion = conectar()
    # #insertar en base de datos
    # if isMedic == 'Si':
    #     if saveEmployeeAndIsMedic(conexion,name,lastname,birthdate,sex,isMedic,cedula,email,password,confirmPassword):
    #         return "<h1>Data received</h1>" + name
    #     else:
    #         return "<p>Error al guardar la informacion</p>"
    # else:
    #     if saveEmployee(conexion,name,lastname,sex,isMedic,email,password,confirmPassword):
    #         return "<h1>Data received</h1>" + name
    #     else:
    #         return "<p>Error al guardar la informacion</p>"
    

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

# Añadiendo proyecto 3
@app.route('/enfermedades')
def enfermedades():
    conexion = conectar()
    if conexion == None:
        return '<p> Error de conexion...</p>'
    else:
        enfermedades = getEnfermedades(conexion)
        print("enfermedades", enfermedades)
        return render_template("enfermedades.html", enfermedades=enfermedades)

if __name__ == '__main__':
    app.run()