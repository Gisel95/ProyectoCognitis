from flask import Flask, render_template, request
import model



app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    return render_template('homepage.html')
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario == usuario and contraseña == contraseña:
            return render_template('inicio.html')
        else:
            error_message = 'No se puede iniciar sesion'
            return render_template('login.html' , message = error_message)

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/registro', methods = ['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template('registro.html')
    else:
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        email = request.form['email']
        if usuario == 'Gisel' and contraseña == 'gigimor' and email == 'ale_g_30@hotmail.com':
            return render_template('inicio.html')
        else:
            error_message = 'No se puede iniciar sesion'
            return render_template('login.html' , message = error_message)

@app.route('/sobremi')
def sobremi():
    return render_template('sobremi.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

@app.route('/alfajores')
def alfajores():
    return render_template('alfajores.html')

@app.route('/torta')
def torta():
    return render_template('torta.html')

@app.route('/donas')
def donas():
    return render_template('donas.html')

@app.route('/navidad')
def navidad():
    return render_template('navidad.html')

@app.route('/pan')
def pan():
    return render_template('pan.html')

@app.route('/cupcakes')
def cupcakes():
    return render_template('cupcakes.html')








if __name__=='__main__':
    app.run(debug=True, port=5000)