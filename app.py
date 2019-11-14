import bottle
import json
from bottle import route, run, static_file, template, request, post, install
from logic.recetas_logic import buscar_recetas
from logic.usuarios_logic import UsuariosLogic
from entities.usuario import Usuario, RecetaFavorita
import canister
from canister import session
from datetime import datetime

app = bottle.Bottle()
app.install(canister.Canister())


@app.route('/')
@app.route('/index')
def index():
    return template('index.tpl', recetas=[], usuario=obtener_usuario_actual())


@app.post('/')
@app.post('/index')
def index():
    query = request.forms.get('query')
    recetas = buscar_recetas(query, obtener_usuario_actual())
    return template('index.tpl', recetas=recetas, usuario=obtener_usuario_actual())


@app.route('/mis_recetas')
def mis_recetas():
    return template('mis_recetas.tpl', recetas=[], usuario=obtener_usuario_actual())


@app.route('/login')
def login():
    session.data['usuario'] = None
    return static_file('login.html', root='./public/')


@app.post('/login')
def login():
    user = request.forms.get('inputUser')
    password = request.forms.get('inputPassword')
    usuarios_logic = UsuariosLogic()
    usuario = usuarios_logic.get_one_by_credentials(user, password)
    if usuario != None:
        session.data['usuario'] = usuario
        return index()
    else:
        return static_file('login.html', root='./public/')


@app.route('/registration')
def registration():
    session.data['usuario'] = None
    return static_file('registration.html', root='./public/')


@app.post('/registration')
def registration():
    try:
        user = request.forms.get('inputUser')
        password = request.forms.get('inputPassword')
        email = request.forms.get('inputEmail')
        usuario = Usuario(usuario=user, contrasenia=password,
                          email=email, recetas_favoritas=[])
        usuarios_logic = UsuariosLogic()
        usuarios_logic.insert(usuario)
        session.data['usuario'] = usuario
        return index()
    except:
        return registration()


@app.post('/grabar_receta_favorita')
def grabar_receta_favorita():
    data = request.json
    id_usuario = data['id_usuario']
    uri = data['uri']
    label = data['label']
    fecha = datetime.now()
    receta_fav = RecetaFavorita(url=uri,
                                descripcion=label,
                                id_usuario=id_usuario,
                                usuario=obtener_usuario_actual(),
                                fecha_hora=fecha)
    usuarios_logic = UsuariosLogic()
    usuarios_logic.insert_receta_favorita(receta_fav)

@app.post('/borrar_receta_favorita')
def borrar_receta_favorita():
    data = request.json
    id_usuario = data['id_usuario']
    uri = data['uri']
    label = data['label']
    usuarios_logic = UsuariosLogic()
    usuarios_logic.remove_receta_favorita(id_usuario, uri, label)

def obtener_usuario_actual():
    if 'usuario' in session.data:
        usuario = session.data['usuario']
        return usuario
    else:
        return None


if __name__ == "__main__":
    app.run(host='localhost', reloader=True, port=8080, debug=True)
