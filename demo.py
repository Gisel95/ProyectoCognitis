from flask import Flask, render_template



app = Flask(__name__)

@app.route('/', methods = ['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/sobremi')
def sobremi():
    return render_template('sobremi.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/tienda')
def tienda():
    return render_template('tienda.html')





if __name__=='__main__':
    app.run(debug=True, port=5000)