import math

class BusquedaBinaria:

    def Busqueda(self, lista, clave, izquierda, derecha):

        """
        Metodo que permite realizar una busqueda binaria de un numero
        Devuelve p si clave está en la lista
        Devuelve -1 si clave no está en lista
        """

        """
        izquierda guarda el inicio de la lista
        derecha guarda el fin de la lista
        """

        while izquierda <= derecha:
            # el punto medio del segmento
            medio = math.floor((izquierda + derecha) / 2)
            # si el medio es igual al valor buscado, lo devuelve
            if lista[medio] == clave:
                return medio
            # si el valor del punto medio es menor que clave, sigue buscando
            # en el segmento de la derecha: [medio+1, der],
            # descartando la izquierda
            elif lista[medio] < clave:
                izquierda = medio + 1
            # sino, sigue buscando en el segmento de la izquierda: [izq, medio-1],
            # descartando la derecha
            else:
                derecha = medio - 1
            # si no salió del ciclo, vuelve a iterar con el nuevo segmento

            # salió del ciclo de manera no exitosa: el valor no fue encontrado
        return -1

def main():
    A = [8, 13, 17, 26, 44, 56, 88, 97]
    b = BusquedaBinaria()
    print(b.Busqueda(A, 20, 0, len(A) - 1))

if __name__ == "__main__":
    main()