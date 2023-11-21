"""
Enunciado:
Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se deben introducir en una lista de 4
filas por 5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo
se tratara. La suma total debe aparecer en la esquina inferior derecha.

Fecha: 21/11/2023.
Autores: Sergio López Fernández.
"""

import random

print("Este programa genera una matriz de 4x5 y muestra la suma de sus filas y columnas.")
print("---------------------------------------------------------------------------------")

# Plantilla de la matriz
"""
        COL 1   COL 2   COL 3   COL 4   COL 5   SUMA
FILA 1  000     000     000     000     000     000
FILA 2  000     000     000     000     000     000
FILA 3  000     000     000     000     000     000
FILA 4  000     000     000     000     000     000
SUMA    000     000     000     000     000     000
"""

TOTAL_NUMBERS = 20
MIN = 100
MAX = 999
ROWS = 4
COLUMNS = 5

matrix = []

# Generamos la matriz
for i in range(ROWS):
    matrix.append([])
    for j in range(COLUMNS):
        matrix[i].append(random.randint(MIN, MAX))

# Mostramos la tabla con las sumas
print("\t\tCOL 1\tCOL 2\tCOL 3\tCOL 4\tCOL 5\tSUMA")

for i in range(ROWS):
    print("FILA", i + 1, end="\t")
    for j in range(COLUMNS):
        print(matrix[i][j], end="\t\t")
    print(sum(matrix[i]))

print("SUMA", end="\t")
for i in range(COLUMNS):
    suma = 0
    for j in range(ROWS):
        suma += matrix[j][i]
    print(suma, end="\t")
print(sum([sum(matrix[i]) for i in range(ROWS)]))
