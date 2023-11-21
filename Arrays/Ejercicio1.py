"""
Enunciado:
Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. Carga las lista number con valores
aleatorios entre 0 y 100. En la lista square se deben almacenar los cuadrados de los valores que hay en number. En la
lista cube se deben almacenar los cubos de los valores que hay en number. A continuación, muestra el contenido de las
tres listas dispuesto en tres columnas.

Fecha: 21/11/2023.
Autores: Sergio López Fernández.
"""

import random

print("Este programa muestra el contenido de tres listas, number, square y cube, con 20 números enteros cada una.")
print("----------------------------------------------------------------------------------------------------------")

MINIMUM_VALUE = 0
MAXIMUM_VALUE = 100
ARRAY_LENGTH = 20

number = [random.randint(MINIMUM_VALUE, MAXIMUM_VALUE) for _ in range(ARRAY_LENGTH)]
square = [num ** 2 for num in number]
cube = [num ** 3 for num in number]

print("number\t\tsquare\t\tcube")
print("-----------------------------")
for i in range(ARRAY_LENGTH):
    print(f"{number[i]:4} {square[i]:12} {cube[i]:10}")
    print("-----------------------------")
