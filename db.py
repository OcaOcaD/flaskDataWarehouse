import mysql.connector
from mysql.connector import Error
from mysql.connector import cursor 

def conectar():
    conexion = None
    try:
        conexion = mysql.connector.connect(host="localhost",user="root", password="1234", database= "medicos")
        if conexion.is_connected():
            print('Connected')
            return conexion
        else:
            return None
    except Error as e:
        print("Failed to connect " + e)

def getListadoPersonas(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return filas

def saveEmployeeAndIsMedic(conexion,name,lastname,birthdate, sex,isMedic,cedula,email,password,confirmPassword):
    exito = False
    cursor = conexion.cursor()
    sql = "INSERT INTO empleados VALUES (null, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
    listado = (name, lastname,birthdate, sex, isMedic,cedula,email,password,confirmPassword)
    cursor.execute(sql, listado)
    num_empleado = cursor.lastrowid
    if num_empleado >0:
        exito = True
    conexion.commit()
    cursor.close()
    conexion.close()
    return exito

def saveEmployee(conexion,name,lastname,birthday,sex,isMedic,email,password,confirmPassword):
    print(name,lastname,birthday,sex,isMedic,email,password,confirmPassword)
    exito = False
    cursor = conexion.cursor()
    sql = "INSERT INTO empleados (nombre,apellidos,fecha_nac,genero,es_medico,IdCard, password, confirmPassword ) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s)"
    listado = (name, lastname,birthday, sex, isMedic,email,password,confirmPassword)
    cursor.execute(sql, listado)
    num_empleado = cursor.lastrowid
    if num_empleado >0:
        exito = True
    conexion.commit()
    cursor.close()
    conexion.close()
    return exito

def guardaEmpleado(conexion, nombre, apellidos, anio, genero):
    exito = False
    cursor = conexion.cursor()
    sql = "INSERT INTO empleados VALUES (null, %s,%s,%s,%s)"
    listado = (nombre, apellidos, anio, genero)
    cursor.execute(sql, listado)
    num_empleado = cursor.lastrowid
    if num_empleado >0:
        exito = True
    conexion.commit()
    cursor.close()
    conexion.close()
    return exito

def getEnfermedades(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM enfermedades")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return filas