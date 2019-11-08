from bottle import route, run, static_file, template, request, post
from logic.logic import buscar_recetas


@route('/')
@route('/index')
def index():
    return template('index.tpl', recetas=[])

@post('/')
@post('/index')
def index():
    query = request.forms.get('query')

    recetas = buscar_recetas(query)

    return template('index.tpl', recetas=recetas)


if __name__ == "__main__":
    run(host='localhost', reloader=True, port=8080, debug=True)
