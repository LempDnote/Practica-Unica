
class Funciones():

    def open(self,archivo):
        archivo = open(archivo,"r")
        listado = []
        for lineas in archivo.readlines():
            self.cadena(self.espacios(lineas),listado)
        archivo.close()
        return listado
    def cadena(self,string,listado):
        #Primer idicador "="
        try:
            nombre,cadena = string.split("=")
        except:
            nombre = ""
            cadena = ""
        numerosC = ""
        funciones = ""
        encontrar = ""
        completo = ""
        #Separacion de lista
        for i in range(len(cadena)):
            if cadena[i].isdigit() or cadena[i] == ",":
                numerosC += cadena[i]
            else:
                funciones = cadena[i:]
                break
        Lnumeros = numerosC.split(",")
        Lnumeros2 = numerosC.split(",")
        for i in range(len(funciones)):
            if funciones[i].upper() == "O":
                Lnumeros = self.ordenar(Lnumeros)
                completo = "O"+nombre+":"+"ORDENADOS = "+",".join(Lnumeros)
                listado.append(completo)
            if funciones[i].upper() == "B":
                Bcadena = funciones[i:]
                cadencia = ""
                for j in range(len(Bcadena)):
                    if Bcadena[j].isdigit() or Bcadena[j] == ",":
                        cadencia += Bcadena[j]
                numeros = cadencia.split(",")
                encontrar = self.buscar(numeros,Lnumeros2)
                completo = "B"+nombre+":"+",".join(Lnumeros2)+" BUSQUEDA POSICIONES="+encontrar
                listado.append(completo)
    def espacios(self,string):
        cadena = list(string)
        for i in cadena:
            if i == " ":
                cadena.remove(i)
        string = "".join(cadena)
        return string
    def ordenar(self,listado):
        for i in range(len(listado)-1):
            for j in range(i+1,len(listado)):
                if int(listado[i]) > int(listado[j]):
                    temp = listado[i]
                    listado[i] = listado[j]
                    listado[j] = temp
        return listado
    def buscar(self,listado1,listado2):
        encontrado = ""
        numeros = []
        for i in listado1:
            for j in range(len(listado2)):
                if int(listado2[j]) == int(i):
                    numeros.append(str(j+1))
        encontrado = ",".join(numeros)
        if encontrado == "":
            encontrado = "NO ENCONTRADO"
        return encontrado
