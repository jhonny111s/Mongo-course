
import pymongo
import bottle
import sys

@bottle.get("/hw1/<n>")
def get_hw1(n):

    connection = pymongo.MongoClient("mongodb://localhost")

    n = int(n)

    db = connection.m101
    collection = db.funnynumbers

    magic = 0

    try:
        # Obtiene todos los registros de la colección
        # con un limite de 1 solo registro y un salto de un numero dado
        # los resultados se ordenan por el campo value
        iter = collection.find({},limit=1, skip=n).sort('value', direction=1)
        for item in iter:
            return str(int(item['value'])) + "\n"
    except Exception as e:
        print ("Error trying to read collection:", type(e), e)


bottle.debug(True)
bottle.run(host='localhost', port=8080)
