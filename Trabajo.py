# -*- coding: utf-8 -*-
"""
Trabajo en Clases

@author: Katherine Gomez
"""

#Solicitud de un recurso a un endpoint sin argumentos
import requests
import json


URL = "https://pokeapi.co/api/v2/pokemon?offset=20&limit=20"

respuesta = requests.get(URL)#guardar los datos que se van extraer

if respuesta.status_code == 200: #recorre todo el URL y extrae la información si es exitosa la muestra
    print('Solicitud exitosa')
    print('Datos: ', respuesta.json())
else:
    print("Error en la solicitud del recurso. Detalles: \n, respuesta.text") # De lo contrario da este error
    
#Solicitud de un recurso a un endpoint con argumentos

#URL = "https://jsonplaceholder.typicode.com/comments?portID=1"
URL = "https://pokeapi.co/api/v2/ability/7/"


if respuesta.status_code == 200:
    print('Solicitud exitosa')
    print('Datos: ', respuesta.json())
else:
    print("Error en la solicitud del recurso. Detalles: \n, respuesta.text")
