from flask import Flask, render_template, request
from flask.wrappers import Request

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
    
    return "<h1>Data received</h1>" + name

if __name__ == '__main__':
    app.run()