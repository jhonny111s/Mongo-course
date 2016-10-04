Semana 1
----------

- En mongo no existen los join ni las transaction para poder mejorar la escalabilidad.
- mongo maneja el formato JSON para representar una entidad como un objeto, ya que es liviano,  eficiente y facil de recorrer como se muestra en `jsonExample.json`
y mongo lo que hace es traducirlo a binario en un formato llamado BSON como se muestra en `bsonExample.bson`.
- Se debe instalar mongo y si usas windows recuerda agregar la ruta al path y crear un directorio `data/db` donde deseemos y finalmente dentro corremos el comando mongod para que cree la base de datos. Los archivos `mongo` y `mongod` son la shell y es el servidor respectivamente.
- Para usar mongo podemos hacerlo por medio de su [shell](https://docs.mongodb.com/getting-started/shell/) o podemos usar un lenguaje de programación con un framework que nos permita interactuar con facilidad,  y claro esta un api para manejar mongo. Tanto bottle como pymongo los podemos instalar con `pip`, el cual viene incluido con python.
- Para este caso se usa el lenguaje de programación python junto con el framework bottle, el cual brinda unas caracteristicas muy simples pero que sirven para demostrar el uso de mongo.
- Para iniciar con el framework [bottle](http://bottlepy.org/docs/dev/index.html) vamos a crear un servidor que solo muestra en el navegador "hello `nombre`" como se muestra en el archivo `hello_bottle.py`, esto para asi acceder a la url `localhost:8080/hello/nombre`.
- Para iniciarnos con [pymongo](https://api.mongodb.com/python/current/index.html) se creo un archivo `pymongo_getting_started.py` donde se crean unos registros y se consulta el primero en ser guardado.
- Se creo el archivo `hello.py` donde se unen bottle con pymongo para al momento de acceder a `localhost:8080` se obtenga el mensaje "hello `nombre`" donde el nombre se obtiene de mongo.
- Para hacer algunas pruebas se creo una base de datos llamada `m101`, para importar esta base de datos nos ubicamos en la raiz de esta carpeta y escribimos `mongorestore dump` donde dump es una carpeta que se genero con `mongodump`. Para más información mirar el archivo `commands-mongo.txt`.
- Para comprobar el dump vamos a la shell de mongo y escribimos el siguiente comando dentro de la base de datos m101 `db.hw1.find()`, el resultado debe contener un item llamado answer igual a 42.
- En el archivo `hw-1-2.py` se va a calcular un numero a partir de la busqueda en la colección `funnynumbers` y la respuesta debe ser 1815.
- En el archivo `hw-1-3.py` se hace uso de bottle y pymongo para brindar una url a la cual se le pasa un parámetro `localhost:80807HW1/5O` donde se debe obtener 53 como resultado.
