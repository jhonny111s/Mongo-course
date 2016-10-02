
import bottle
import pymongo

@bottle.route('/')
def index():

    # Conexion a la base de datos
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test

    # Nombre de la coleccion con la que vamos a trabajar
    name = db.names

    # comando para obtener solo el primer registro.
    item = name.find_one()

    return '<b>Hello %s!</b>' % item['name']


bottle.run(host='localhost', port=8080)
