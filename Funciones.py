
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
                Lnumeros = self.ordenar(self.iteracion(Lnumeros))
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
                completo = "B"+nombre+":"+",".join(Lnumeros2)+" BUSQUEDA "+cadencia+" = "+encontrar
                listado.append(completo)
    def espacios(self,listado):
        string = ""
        for i in range(len(listado)):
            if listado[i] != " ":
                string += listado[i]
        return string
    def ordenar(self,listado):
        for i in range(len(listado)-1):
            for j in range(i+1,len(listado)):
                if listado[i] > listado[j]:
                    temp = listado[i]
                    listado[i] = listado[j]
                    listado[j] = temp

        return self.iteracion2(listado)
    def buscar(self,listado1,listado2):
        encontrado = ""
        numeros = []
        for i in listado1:
            for j in range(len(listado2)):
                if listado2[j].isdigit:
                    if listado2[j]== i:
                        numeros.append(str(j+1))
        encontrado = ",".join(numeros)
        if encontrado == "":
            encontrado = "NO ENCONTRADO"
        return encontrado
    def iteracion(self,cadena):
        for i in range(len(cadena)):
            cadena[i] = int(cadena[i])
        return cadena
    def iteracion2(self,numeros):
        for i in range(len(numeros)):
            numeros[i] = str(numeros[i])
        return numeros

