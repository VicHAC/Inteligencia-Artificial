from time import perf_counter  # Importa perf_counter para mayor precisión
import tracemalloc  # Importa tracemalloc para medir el uso de memoria

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
    indice = 0  # Índice para recorrer la cola

    while indice < len(cola):
        nodoActual = cola[indice]  # Acceder al primer nodo usando el índice
        recorrido += str(nodoActual.dato) + " "  # Agregar al recorrido
        indice += 1  # Avanzar el índice para simular el "pop"

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
    indice = len(pila) - 1  # Inicializar el índice al último elemento de la pila

    while indice >= 0:
        nodoActual = pila[indice]  # Acceder al último nodo usando el índice
        recorrido += str(nodoActual.dato) + " "  # Agregar al recorrido
        indice -= 1  # Retroceder el índice para simular el "pop"

        # Verificar si hemos encontrado el nodo buscado
        if nodoActual.dato == nodoAEncontrar:
            break  # Detener la búsqueda si encontramos el nodo

        # Agregar los hijos del nodo actual a la pila (en orden inverso)
        pila.extend(reversed(nodoActual.hijos))
        indice = len(pila) - 1  # Actualizar el índice al último nodo

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

    # Iniciar el rastreo de memoria
    tracemalloc.start()

    # Hacer los recorridos BFS y DFS desde el nodo inicial
    bfs(nodo1, nodoAEncontrar)
    dfs(nodo1, nodoAEncontrar)

    # Obtener estadísticas de memoria después de la ejecución
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    print(f"Memoria actual usada: {memoria_actual / 1024:.2f} KB")
    print(f"Memoria pico usada: {memoria_pico / 1024:.2f} KB")

    # Detener el rastreo de memoria
    tracemalloc.stop()

# Iniciar programa
if __name__ == "__main__":
    main()