
class Funcinoes():

    def __init__(self):
        self.open("gola")
        return None

    def open(self,archivo):
        archivo = open("Datos.txt","r")
        for lineas in archivo.readlines():
            self.cadena(self.espacios(lineas))
        archivo.close()
        return 0

    def cadena(self,string):
        #Primer idicador "="
        nombre,cadena = string.split("=")
        numerosC = ""
        funciones = ""
        #Separacion de lista
        for i in range(len(cadena)):
            if cadena[i].isdigit() or cadena[i] == ",":
                numerosC += cadena[i]
            else:
                funciones = cadena[i:]
                break
        Lnumeros = numerosC.split(",")
        for i in range(len(funciones)):
            if funciones[i].upper() == "O":
                Lnumeros.sort()
            if funciones[i].upper() == "B":
                Bcadena = funciones[i:]
                cadencia = ""
                for j in range(len(Bcadena)):
                    if Bcadena[j].isdigit() or Bcadena[j] == ",":
                        cadencia += Bcadena[j]

    def espacios(self,string):
        cadena = list(string)
        for i in cadena:
            if i == " ":
                cadena.remove(i)
        string = "".join(cadena)
        return string
    def archivo(self,nombre,funcion,lista):
        cadena = nombre+":"+" "+funcion+"="+"".join(lista)
        print(cadena)
    def busqueda(self,busqueda,lista):
        listado = busqueda.split(",")
        
        return 0

Funcinoes()