'''
Ejercicio 1: Crea un aplicación web basica con flask que al ser ejecutada. inicia un servidor local en el puerto 5000.
Cuando visite la ruta principal (http:/localhost:5000/)
El servidor debera responder con un mensaje HTML que dice "Hello, Word Flask"
'''
#Se importa el modulo de flask desde el paquete flask
from flask import Flask

#Crear una instancia de la clase flask
'''El argurmento __name__ le dice a Flask
Que utilice el nombre del archivo actual main.py'''
app = Flask(__name__)


''' Este es un decorador que define una 
corresponde a la pagina principal de la app'''
@app.route('/')


#Cuando alguien visite app (Por ejemplo. http://localhost:5000/)
#La función hello() séra ejecutada 
def hello():
    return '¡Holaaa mundo!'


#Solo se ejecuta si el archivo es ejecutado directamente
#Aranca la aplicación Falsk en modo depuración (debug-true)
if __name__ == '__main__':
    app.run(debug=True,port=5000)
