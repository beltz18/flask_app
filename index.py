from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

users = []

@app.route('/')
def index():
  return render_template('index.html', num_users=len(users), user=users)

@app.route('/add_user/<string:user>/')
def show_users(user):
  users.append(user)
  return f"Se ha agregado el usuario: {user}"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    name = request.form['name']
    emai = request.form['email']
    pasw = request.form['password']
    user = {
      "name": name,
      "email": emai,
      "password": pasw
    }
    users.append(user)

    next = request.args.get('next', None)
    if(next):
      return redirect(next)
    return redirect(url_for('index'))
  return render_template('signup.html')

# para correr la app:
# export FLASK_APP="nombre_archivo.py" en Linux o set "FLASK_APP=nombre_archivo.py" en Windows
# salir del entorno con deactivate y volver a entrar
# correr el comando flask run