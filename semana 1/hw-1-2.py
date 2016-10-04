import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.m101
collection = db.funnynumbers

magic = 0

try:
    # Obtiene todos los registros de la colección
    iter = collection.find()
    for item in iter:
        # solo se suman los multiplos de 3
        if ((item['value'] % 3) == 0):
            magic = magic + item['value']
except Exception as e:
    print ("Error trying to read collection:", type(e), e)


print("The answer to Homework One, Problem 2 is " + str(int(magic)))
