from binario import arbolBinario

def main():
    Lista = []
    Lista.extend(range(500,-1,-1))
    arbol = arbolBinario()

    print("Arreglo desordenado: \t",Lista)
    #arbol.ordenar(Lista)
    print("Arreglo Ordenado:\t",arbol.ordenar(Lista))

if __name__ == '__main__':
    main()
