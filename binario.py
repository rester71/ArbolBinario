#Implementacion de un algoritmo de ordenamiento Arbol binario

#Se necesita una clase nodo, para actual como una estructura
class Nodo(object):
    def __init__(self,valor):
        self.izquierdo = None
        self.valor = valor
        self.derecho = None

class arbolBinario(object):
    #Simple variable donde se almacenara el arreglo ordenado
    lista_ordenada = []
    #Funcion que crea un Nodo
    def crear(self,valor):
        return Nodo(valor)
    #Funcion que inserta un nodo en el arbol, si este no existe, lo crea
    def insertar(self, nodo, valor):
        #Si el arlbol esta vacio creo un nuevo nodo
        if nodo is None:
            return self.crear(valor)
        #Si el valor que entra es menor que el valor del nodo, se inserta un nuevo nodo
        #el la posicion izquerda
        if valor < nodo.valor:
            nodo.izquierdo = self.insertar(nodo.izquierdo, valor)
        #De lo contrario se inserta en en laparte derecha
        elif valor > nodo.valor:
            nodo.derecho = self.insertar(nodo.derecho, valor)
        return nodo
    #Funcion que agrega el valor de los nodos recorriendo el arbol de forma
    #Inorden( izq, raiz, der)
    def agregarLista(self, nodo):
        if nodo is not None:
            self.agregarLista(nodo.izquierdo)
            self.lista_ordenada.append(nodo.valor)
            self.agregarLista(nodo.derecho)

    #Funcion que ordena el la lista y devulve la lista ya ordenada
    def ordenar(self, lista):
        #self.lista_ordenada = lista
        nodoRaiz = None
        nodoRaiz = self.insertar(nodoRaiz,lista[0])
        for valor in lista[1:]:
            self.insertar(nodoRaiz, valor)
        self.agregarLista(nodoRaiz)
        lista = self.lista_ordenada
        self.lista_ordenada = []
        return lista
