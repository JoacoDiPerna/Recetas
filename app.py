import bottle
from bottle import route, run, static_file, template, request, post, install
from logic.logic import buscar_recetas
from logic.usuarios_logic import SociosLogic
from entities.usuario import Usuario
import canister
from canister import session

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

    recetas = buscar_recetas(query)

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
    socios_logic = SociosLogic()
    usuario = socios_logic.get_one_by_credentials(user, password)
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
        socios_logic = SociosLogic()
        socios_logic.insert(usuario)
        session.data['usuario'] = usuario
        return index()
    except:
        return registration()


def obtener_usuario_actual():
    if 'usuario' in session.data:
        usuario = session.data['usuario']
        return usuario
    else:
        return None


if __name__ == "__main__":
    app.run(host='localhost', reloader=True, port=8080, debug=True)
