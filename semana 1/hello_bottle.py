# se importa las librerias de bottle que necesitamos
from bottle import route, run, template

# esta es la ruta que se definio para esta funcionalidad
@route('/hello/<name>')
def index(name):
    # Genera un html donde se remplaza name por lo que se envie en la url
    return template('<b>Hello {{name}}</b>!', name=name)

# Inicializa el servidor con el dirección y puerto indicado
run(host='localhost', port=8080)
