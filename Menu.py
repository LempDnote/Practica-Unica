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
                print("En proceso")
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
        return 0