# clase para representar un nodo en el arbol
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

# funcion para hacer la busqueda en anchura (bfs)
def bfs(nodoInicial, nodoAEncontrar):
    cola = [nodoInicial]  # lista para la cola
    recorrido = ""  # variable para almacenar el recorrido

    while len(cola) > 0:
        # sacar el primer nodo de la cola
        nodoActual = cola.pop(0)
        recorrido += str(nodoActual.dato) + " "  # agregar a la cadena de recorrido

        # verificar si hemos encontrado el nodo buscado
        if nodoActual.dato == nodoAEncontrar:
            break  # detener la busqueda si encontramos el nodo

        # agregar los hijos del nodo actual a la cola
        for hijo in nodoActual.hijos:
            cola.append(hijo)

    # imprimir los nodos recorridos
    print("recorrido bfs:", recorrido)

# funcion para hacer la busqueda en profundidad (dfs)
def dfs(nodoInicial, nodoAEncontrar):
    pila = [nodoInicial]  # lista para la pila
    recorrido = ""  # variable para almacenar el recorrido

    while len(pila) > 0:
        # sacar el ultimo nodo de la pila
        nodoActual = pila.pop()
        recorrido += str(nodoActual.dato) + " "  # agregar a la cadena de recorrido

        # verificar si hemos encontrado el nodo buscado
        if nodoActual.dato == nodoAEncontrar:
            break  # detener la busqueda si encontramos el nodo

        # agregar los hijos del nodo actual a la pila (en orden inverso)
        for hijo in reversed(nodoActual.hijos):
            pila.append(hijo)

    # imprimir los nodos recorridos
    print("recorrido dfs:", recorrido)

# funcion para construir el arbol
def crearArbol():
    nodo1 = Nodo(1)   # capa 1
    nodo2 = Nodo(2)   # capa 2
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)   # capa 3
    nodo5 = Nodo(5)
    nodo6 = Nodo(6)
    nodo7 = Nodo(7)

    # asignar los hijos a cada nodo
    nodo1.hijos = [nodo2, nodo3]
    nodo2.hijos = [nodo4, nodo5]
    nodo3.hijos = [nodo6, nodo7]

    return nodo1

# funcion principal
def main():
    # crear el arbol
    nodo1 = crearArbol()

    # pedir al usuario que elija el nodo a buscar
    nodoAEncontrar = int(input("elige el nodo a buscar: "))

    # hacer los recorridos bfs y dfs desde el nodo inicial
    bfs(nodo1, nodoAEncontrar)
    dfs(nodo1, nodoAEncontrar)

# iniciar programa
main()
