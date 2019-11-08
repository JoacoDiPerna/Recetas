import requests
import json
from entities.entities import Receta


def buscar_recetas(query):
    api_url = 'https://test-es.edamam.com/search?q=' + \
        str(query) + '&from=0&to=100'

    recetas = []
    contador = 0

    r = requests.get(api_url)

    res = (json.loads(r.text))['hits']

    for result in res:
        if contador == 12:
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
        # if existe_imagen(image):
        if pagina_con_imagen(url):
            recetas.append(receta)
            contador += 1

    return recetas


def pagina_con_imagen(url):
    if 'http://www.elle.es/' in url or 'http://www.comidakraft.com/' in url or 'http://www.recetasgratis.net/' in url or 'http://www.hogarmania.com/' in url or 'http://www.kiwilimon.com/' in url or 'https://www.hogarmania.com/' in url:
        return False
    else:
        return True


def existe_imagen(url):
    try:
        r = requests.head(url, timeout=0.3)
        if r.status_code == requests.codes.ok:
            return True
    except:
        return False
