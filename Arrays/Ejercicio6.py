"""
Enunciado:
Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

Fecha: 21/11/2023.
Autores: Sergio López Fernández.
"""

import numpy as np

print("Este programa genera una matriz de 4x5 y muestra la suma de sus filas y columnas.")
print("---------------------------------------------------------------------------------")

TOTAL_NUMBERS = 20
MIN = 100
MAX = 999
ROWS = 4
COLUMNS = 5

# Generamos la matriz
matrix = np.random.randint(MIN, MAX, size=(ROWS, COLUMNS))

# Mostramos la tabla con las sumas
print("\t\tCOL 1\tCOL 2\tCOL 3\tCOL 4\tCOL 5\tSUMA")

for i in range(ROWS):
    print("FILA", i + 1, end="\t")
    for j in range(COLUMNS):
        print(matrix[i][j], end="\t\t")
    print(np.sum(matrix[i]))

print("SUMA", end="\t")
for i in range(COLUMNS):
    suma = np.sum(matrix[:, i])
    print(suma, end="\t")
print(np.sum(matrix))
