from ConsultaDeDatos import *
class ImplentacionDeLaBusqueda:


    """
    Metodo que abre y lee el archivo llamado "datos",
    en el cada uno de sus elemntos se separa por una ","
    """
    def leerArchivo(self, archivo):
        datos = []

        file = open(archivo, 'r')
        for f in file.readlines():
            linea = f.replace('\n', '')
            elementos = linea.split(',')
            try:
                datos.append([str(elementos[0]), int(elementos[1])])

            except ValueError:
                datos.append(['', 0.0])

        file.close()
        del (file)
        return datos


    """
    Metodo que generan los resultados, en el que obtiene como
    parametro la lista y el dato que se desea encontrar, realizando asi
    una busqueda secuencial. 
    """
    def generarResultados(self, lista,datoencontrar):

        rectangulo = BusquedaSecuencial()
        resultados = []
        for f in range(0, len(lista)):
            area = rectangulo.busqueda(lista,datoencontrar)
            resultados.append([area])
        return resultados

    """
    Metodo que permite guardar los resultados en otro archivo,
    llamado como "ResultadosDeBusqueda.txt"
    """
    def guardarResultados(self, archivo, datos, resultados):
        file = open(archivo, 'w')
        for f in range(0, len(datos)):
            linea =  str(resultados[f][0]) + ',' + '\n'
            file.write(linea)
        file.close()
        del (file)

def main():
    file = ImplentacionDeLaBusqueda()
    datoAencontrar = 7676798567   #Se asigna el dato que se desea encontrar
    arreglo = file.leerArchivo('datos.txt')   #Se leee el archivo "datos"
    resultados = file.generarResultados(arreglo,datoAencontrar)  #Genera los resultados
    file.guardarResultados('ResultadosDeBusqueda.txt', arreglo, resultados)   #Guarda los resultados en un nuevo archivo


