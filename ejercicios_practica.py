#!/usr/bin/env python
'''
JSON ETL [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import matplotlib.pyplot as plt

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas
    json_data = {
        "Nombre":"Marta",
        "Apellido":"Fort",
        "DNI": 14354867,
        "prendas" : [
            {"prenda": "zapatilla",
            "cantidad": 4
            },
            {"prenda": "remeras",
            "cantidad": 12
            }]
            }                                                                                                   

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    with open('mi_json.json', 'w') as jsonfile:
        datos = [json_data]
        json.dump(datos, jsonfile, indent=4)
    
    # Observe el archivo y verifique que se almaceno lo deseado
    pass


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    with open('mi_json.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1

    json_string = json.dumps(json_data, indent=4)
    print(json_string)

    pass


def ej3():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    data = response.json()
    

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.    
    user1 = []
    completed1 = 0
    for user in data:
        if user['userId'] == 1:
            user1.append(user)
    for completo in user1:
        if completo["completed"] == True:
            completed1 += 1

    user2 = []
    completed2 = 0
    for user in data:
        if user['userId'] == 2:
            user2.append(user)
    for completo in user2:
        if completo["completed"] == True:
            completed2 += 1

    user3 = []
    completed3 = 0
    for user in data:
        if user['userId'] == 3:
            user3.append(user)
    for completo in user2:
        if completo["completed"] == True:
            completed3 += 1    

    user4 = []
    completed4 = 0
    for user in data:
        if user['userId'] == 4:
            user4.append(user)
    for completo in user4:
        if completo["completed"] == True:
            completed4 += 1

    user5 = []
    completed5 = 0
    for user in data:
        if user['userId'] == 5:
            user5.append(user)
    for completo in user5:
        if completo["completed"] == True:
            completed5 += 1

    user6 = []
    completed6 = 0
    for user in data:
        if user['userId'] == 6:
            user6.append(user)
    for completo in user6:
        if completo["completed"] == True:
            completed6 += 1

    user7 = []
    completed7 = 0
    for user in data:
        if user['userId'] == 7:
            user7.append(user)
    for completo in user7:
        if completo["completed"] == True:
            completed7 += 1

    user8 = []
    completed8 = 0
    for user in data:
        if user['userId'] == 8:
            user8.append(user)
    for completo in user8:
        if completo["completed"] == True:
            completed8 += 1

    user9 = []
    completed9 = 0
    for user in data:
        if user['userId'] == 9:
            user9.append(user)
    for completo in user9:
        if completo["completed"] == True:
            completed9 += 1

    user10 = []
    completed10 = 0
    for user in data:
        if user['userId'] == 10:
            user10.append(user)
    for completo in user10:
        if completo["completed"] == True:
            completed10 += 1            

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    completed = [completed1,completed2,completed3,completed4,completed5,
                completed6,completed7,completed8,completed9,completed10]
    userId = ["userId 1","userId 2","userId 3","userId 4","userId 5",
            "userId 6","userId 7","userId 8","userId 9","userId 10"]

    plt.pie(completed, labels=userId)
    plt.legend(completed,
          title="Completed",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    plt.axis("equal")
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
