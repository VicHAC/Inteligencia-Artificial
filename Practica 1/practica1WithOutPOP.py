from time import perf_counter  # Importa perf_counter para mayor precisión
import tracemalloc  # Importa tracemalloc para medir el uso de memoria

# Clase para representar un nodo en el árbol
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

# Función para hacer la búsqueda en anchura (BFS)
def bfs(nodoInicial, nodoAEncontrar):
    tracemalloc.start()  # Iniciar rastreo de memoria para BFS
    start_time = perf_counter()  # Tiempo inicial
    cola = [None] * 100  # Cola predefinida con espacio suficiente
    recorrido = ""  # Variable para almacenar el recorrido
    indiceInsercion = 0  # Índice para insertar nodos
    indiceLectura = 0  # Índice para leer nodos

    cola[indiceInsercion] = nodoInicial
    indiceInsercion += 1

    while indiceLectura < indiceInsercion:
        nodoActual = cola[indiceLectura]  # Leer el nodo actual usando el índice de lectura
        recorrido += str(nodoActual.dato) + " "  # Agregar al recorrido
        indiceLectura += 1  # Avanzar el índice de lectura

        # Verificar si hemos encontrado el nodo buscado
        if nodoActual.dato == nodoAEncontrar:
            break  # Detener la búsqueda si encontramos el nodo

        # Insertar los hijos del nodo actual en la cola
        for i in range(len(nodoActual.hijos)):
            cola[indiceInsercion] = nodoActual.hijos[i]
            indiceInsercion += 1

    # Imprimir los nodos recorridos
    print("Recorrido BFS:", recorrido)
    end_time = perf_counter()  # Tiempo final
    execution_time = (end_time - start_time) * 1e6  # Convertir a microsegundos
    print(f"Tiempo de ejecución de BFS: {execution_time:.2f} microsegundos")

    # Obtener estadísticas de memoria para BFS
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    print(f"Memoria utilizada por BFS: {memoria_actual / 1024:.2f} KB")
    print()
    tracemalloc.stop()  # Detener rastreo de memoria para BFS

# Función para hacer la búsqueda en profundidad (DFS)
def dfs(nodoInicial, nodoAEncontrar):
    tracemalloc.start()  # Iniciar rastreo de memoria para DFS
    start_time = perf_counter()  # Tiempo inicial
    pila = [None] * 100  # Pila predefinida con espacio suficiente
    recorrido = ""  # Variable para almacenar el recorrido
    indiceInsercion = 0  # Índice para insertar nodos
    indiceLectura = 0  # Índice para leer nodos

    pila[indiceInsercion] = nodoInicial
    indiceInsercion += 1

    while indiceInsercion > 0:
        indiceInsercion -= 1
        nodoActual = pila[indiceInsercion]  # Leer el nodo actual de la pila
        recorrido += str(nodoActual.dato) + " "  # Agregar al recorrido

        # Verificar si hemos encontrado el nodo buscado
        if nodoActual.dato == nodoAEncontrar:
            break  # Detener la búsqueda si encontramos el nodo

        # Insertar los hijos del nodo actual en la pila en orden inverso
        for i in range(len(nodoActual.hijos)-1, -1, -1):
            pila[indiceInsercion] = nodoActual.hijos[i]
            indiceInsercion += 1

    # Imprimir los nodos recorridos
    print("Recorrido DFS:", recorrido)
    end_time = perf_counter()  # Tiempo final
    execution_time = (end_time - start_time) * 1e6  # Convertir a microsegundos
    print(f"Tiempo de ejecución de DFS: {execution_time:.2f} microsegundos")

    # Obtener estadísticas de memoria para DFS
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    print(f"Memoria utilizada por DFS: {memoria_actual / 1024:.2f} KB")
    tracemalloc.stop()  # Detener rastreo de memoria para DFS

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
