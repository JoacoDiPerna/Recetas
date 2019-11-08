import requests
import json
from bottle import route, run, static_file, template, request, post
from entities.entities import Receta


@route('/')
@route('/index')
def index():
    return template('index.tpl', recetas=[])


@post('/index')
def index():
    query = request.forms.get('query')

    api_url = 'https://test-es.edamam.com/search?q=' + str(query) + '&from=0&to=40'

    recetas = []
    contador = 0

    r = requests.get(api_url)

    res = (json.loads(r.text))['hits']

    for result in res:
        if contador==12:
            break
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
        if existe_imagen(image):
            recetas.append(receta)
            contador+=1

    return template('index.tpl', recetas=recetas)


def existe_imagen(url):
    try:
        r = requests.head(url)
        if r.status_code == requests.codes.ok:
            return True
    except:
        return False


if __name__ == "__main__":
    run(host='localhost', reloader=True, port=8080, debug=True)
