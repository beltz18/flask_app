from flask import Flask, render_template
app = Flask(__name__)

users = []

@app.route('/')
def index():
  return render_template('index.html', num_users=len(users), user=users)

@app.route('/add_user/<string:user>/')
def show_users(user):
  users.append(user)
  return f"Se ha agregado el usuario: {user}"

# para correr la app:
# export FLASK_APP="nombre_archivo.py" en Linux o set "FLASK_APP=nombre_archivo.py" en Windows
# salir del entorno con deactivate y volver a entrar
# correr el comando flask run