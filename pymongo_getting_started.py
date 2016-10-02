
import pymongo

from pymongo import MongoClient


# Conexion a la base de datos
connection = MongoClient('localhost', 27017)
db = connection.test

# Nombre de la coleccion con la que vamos a trabajar
names = db.names

# Registros que se van a guardar en la colleccion names
dictionary = [
{"name": "pedro"},
{"name": "juan"},
{"name": "carlos"},
{"name": "maria"},
{"name": "camila"}
]

# Se eliman todos los registros existentes en names
# ya que a modo de ejemplo cada que corramos el archivos
# solo se conservaran los 5 registros.
names.remove()

# Comando para insertar los regristros
save = names.insert_many(dictionary)

# se muestras los id de cada registro guardado
print(save.inserted_ids)

# Comando para obtener todos los regristros
get = names.find()

# se muestra el nombre del primer registro.
# para mostrar cada registro debe recorrerse
# el cursor que se retorna por el find().
print(get[0]['name'])
