class BusquedaSecuencial:


    """
    Metodo que realiza una busqueda secuencial, para
    encontrar un telefono cualquiera, ya que si existe devuelve un True
    y si no existe un False.
    """
    def busqueda(self, lista, clave):

        encontrado = False
        for f in range(0, len(lista)):
            for c in range(0, len(lista[f])):
                if lista[f][c] == clave:
                    encontrado = True
                    break
        return encontrado

