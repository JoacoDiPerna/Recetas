import requests
import json
from bottle import route, run, static_file, template, request, post
from entities.entities import Receta


@route('/')
@route('/index')
def index():
    return template('index.tpl', recetas=[])


@post('/buscar_receta')
def buscar_receta():
    query = request.forms.get('query')

    api_url = 'https://test-es.edamam.com/search?q=' + str(query)

    recetas = []

    r = requests.get(api_url)

    res = (json.loads(r.text))['hits']

    for result in res:
        uri = result['recipe']['uri']
        label = result['recipe']['label']
        image = result['recipe']['image']
        source = result['recipe']['source']
        url = result['recipe']['url']
        calories = round(result['recipe']['calories'])
        ingredientes = []
        for ingredient in result['recipe']['ingredientLines']:
            ingredientes.append(ingredient)
        receta = Receta(uri, label, image, source, url, calories, ingredientes)
        recetas.append(receta)

    return template('index.tpl', recetas=recetas)


if __name__ == "__main__":
    index()
    run(host='localhost', reloader=True, port=8080, debug=True)
