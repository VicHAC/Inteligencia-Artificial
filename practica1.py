# Clase para representar un nodo en el árbol
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

# Función para hacer la búsqueda en anchura (BFS)
def BFS(nodo_inicial):
    cola = [nodo_inicial]  # Usamos una lista para la cola
    print("Recorrido BFS: ", end="")

    while len(cola) > 0:
        # Sacar el primer nodo de la cola
        nodo_actual = cola.pop(0)
        print(nodo_actual.dato, end=" ")

        # Agregar los hijos del nodo actual a la cola
        for hijo in nodo_actual.hijos:
            cola.append(hijo)

    print()

# Función para hacer la búsqueda en profundidad (DFS)
def DFS(nodo_inicial):
    pila = [nodo_inicial]  # Usamos una lista para la pila
    print("Recorrido DFS: ", end="")

    while len(pila) > 0:
        # Sacar el último nodo de la pila
        nodo_actual = pila.pop()
        print(nodo_actual.dato, end=" ")

        # Agregar los hijos del nodo actual a la pila (en orden inverso)
        for hijo in reversed(nodo_actual.hijos):
            pila.append(hijo)

    print()

# Función principal para construir el árbol y hacer los recorridos
def main():
    # Crear los nodos del árbol
    raiz = Nodo(1)   # Capa 1
    nodo2 = Nodo(2)  # Capa 2
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)  # Capa 3
    nodo5 = Nodo(5)
    nodo6 = Nodo(6)
    nodo7 = Nodo(7)

    # Construir el árbol: asignar los hijos a cada nodo
    raiz.hijos = [nodo2, nodo3]
    nodo2.hijos = [nodo4, nodo5]
    nodo3.hijos = [nodo6, nodo7]

    # Pedir al usuario que elija el nodo inicial
    print("Nodos disponibles: 1, 2, 3, 4, 5, 6, 7")
    opcion = int(input("Elige el nodo inicial para el recorrido (1-7): "))

    # Seleccionar el nodo inicial según la opción elegida
    if opcion == 1:
        nodo_inicial = raiz
    elif opcion == 2:
        nodo_inicial = nodo2
    elif opcion == 3:
        nodo_inicial = nodo3
    elif opcion == 4:
        nodo_inicial = nodo4
    elif opcion == 5:
        nodo_inicial = nodo5
    elif opcion == 6:
        nodo_inicial = nodo6
    elif opcion == 7:
        nodo_inicial = nodo7
    else:
        print("Opción no válida.")
        return

    # Hacer los recorridos BFS y DFS
    BFS(nodo_inicial)
    DFS(nodo_inicial)

# Llamar a la función principal
if __name__ == "__main__":
    main()
