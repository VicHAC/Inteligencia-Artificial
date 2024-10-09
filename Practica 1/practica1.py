from time import perf_counter  # Importa perf_counter para mayor precisión

# Clase para representar un nodo en el árbol
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

# Función para hacer la búsqueda en anchura (BFS)
def bfs(nodoInicial, nodoAEncontrar):
    start_time = perf_counter()  # Tiempo inicial
    cola = [nodoInicial]  # Lista para la cola
    recorrido = ""  # Variable para almacenar el recorrido
#VIC
    while cola:
        # Sacar el primer nodo de la cola
        nodoActual = cola.pop(0)
        recorrido += str(nodoActual.dato) + " "  # Agregar al recorrido

        # Verificar si hemos encontrado el nodo buscado
        if nodoActual.dato == nodoAEncontrar:
            break  # Detener la búsqueda si encontramos el nodo

        # Agregar los hijos del nodo actual a la cola
        cola.extend(nodoActual.hijos)

    # Imprimir los nodos recorridos
    print("Recorrido BFS:", recorrido)
    end_time = perf_counter()  # Tiempo final
    execution_time = (end_time - start_time) * 1e6  # Convertir a microsegundos
    print(f"Tiempo de ejecución de BFS: {execution_time:.2f} microsegundos")

# Función para hacer la búsqueda en profundidad (DFS)
def dfs(nodoInicial, nodoAEncontrar):
    start_time = perf_counter()  # Tiempo inicial
    pila = [nodoInicial]  # Lista para la pila
    recorrido = ""  # Variable para almacenar el recorrido

    while pila:
        # Sacar el último nodo de la pila
        nodoActual = pila.pop()
        recorrido += str(nodoActual.dato) + " "  # Agregar al recorrido

        # Verificar si hemos encontrado el nodo buscado
        if nodoActual.dato == nodoAEncontrar:
            break  # Detener la búsqueda si encontramos el nodo

        # Agregar los hijos del nodo actual a la pila (en orden inverso)
        pila.extend(reversed(nodoActual.hijos))

    # Imprimir los nodos recorridos
    print("Recorrido DFS:", recorrido)
    end_time = perf_counter()  # Tiempo final
    execution_time = (end_time - start_time) * 1e6  # Convertir a microsegundos
    print(f"Tiempo de ejecución de DFS: {execution_time:.2f} microsegundos")

# Función para construir el árbol
def crearArbol():
    nodo1 = Nodo(1)   # Capa 1
    nodo2 = Nodo(2)   # Capa 2
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)   # Capa 3
    nodo5 = Nodo(5)
    nodo6 = Nodo(6)
    nodo7 = Nodo(7)

    # Asignar los hijos a cada nodo (grafo no dirigido)
    nodo1.hijos = [nodo2, nodo3]
    nodo2.hijos = [nodo4, nodo5]
    nodo3.hijos = [nodo6, nodo7]

    return nodo1

# Función principal
def main():
    # Crear el árbol
    nodo1 = crearArbol()

    # Pedir al usuario que elija el nodo a buscar
    nodoAEncontrar = int(input("Elige el nodo a buscar: "))

    # Hacer los recorridos BFS y DFS desde el nodo inicial
    bfs(nodo1, nodoAEncontrar)
    dfs(nodo1, nodoAEncontrar)

# Iniciar programa
if __name__ == "__main__":
    main()

