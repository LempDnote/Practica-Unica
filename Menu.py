import json
import webbrowser

from Funciones import Funciones
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Menuinicial():
    def __init__(self):
        self.opciones()
    def opciones(self):
        Funcion = Funciones()
        lista = []
        bandera = True
        while bandera:
            print("Elija una opcion:\n"
                  "1. CARGAR ARCHIVO DE ENTRADA\n"
                  "2. DESPLEGAR LISTAS ORDENADAS\n"
                  "3. DESPLEGAR BUSQUEDAS\n"
                  "4. DESPLEGAR TODAS\n"
                  "5. DESPLEGAR TODAS A ARCHIVO\n"
                  "6. SALIR"
                  )
            opcion = int(input("@>> "))
            if opcion == 1:
                ventana = Tk()
                ventana.withdraw()
                ventana.update()
                path = askopenfilename()
                if path:
                    lista = Funcion.open(path)
            if opcion == 2:
                self.Seleccion(lista,"O")
            if opcion == 3:
                self.Seleccion(lista,"B")
            if opcion == 4:
                self.Todas(lista)
            if opcion == 5:
                self.Todas_Archivo(lista)
            if opcion == 6:
                print("Adios!")
                bandera = False
    def Seleccion(self,lista,valor):
        for i in lista:
            if i[0] == valor:
                print(i[1:])
    def Todas(self,lista):
        for i in lista:
            print(i[1:])
    def Todas_Archivo(self,lista):
        cadena = ""
        Dom = []
        lista2 = []
        for i in lista:
            lista2.append(i[1:])
        for i in range(len(lista2)):
            Dom.append({"Listado":lista2[i]})
        with open('Plantillas/archivo.json','w') as f:
            json.dump(Dom,f,indent=2)
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(
            "http://localhost:63342/Practica%20Unica/Plantillas/index.html?_ijt=md08kv50qg9akhg2rev2fl8kbt")