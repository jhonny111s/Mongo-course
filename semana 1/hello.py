# Se importan las librerias necesarias para usar mongo y las urls
import bottle
import pymongo

# Se define la funcionalidad para la url raiz /
@bottle.route('/')
def index():

# Inicializa host y puerto de la Conexion
connection = MongoClient('localhost', 27017)

# Conexion a la base de datos llamada test
db = connection.test

    # Nombre de la coleccion con la que vamos a trabajar
    name = db.names

    # comando para obtener solo el primer registro.
    item = name.find_one()

    # Genera un html donde se usa el item consultado desde mongo
    return '<b>Hello %s!</b>' % item['name']

# Inicializa el servidor con el dirección y puerto indicado
bottle.run(host='localhost', port=8080)
