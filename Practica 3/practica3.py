import matplotlib.pyplot as plt

def crearLaberinto():
    laberinto = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
    ]
    return laberinto

laberinto = crearLaberinto()

# Imprimir la matriz
for fila in laberinto:
    print(' '.join(map(str, fila)))

plt.imshow(laberinto, cmap='binary')
plt.show()

# Pedir al usuario que ingrese una coordenada
fila = int(input("Ingresa la fila (0-7): "))
columna = int(input("Ingresa la columna (0-14): "))


# plt.imshow (laberinto, cmap='binary') -> lienzo sin datos
# plt.plot (pos[1], pos[0], 'o', color='red')
# plt.show() -. muestra los datos al lienzo
# plt.figure() -> muestra en otra pagina otro lienzo con los datos