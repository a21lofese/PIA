"""
Enunciado:
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy.
El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y
todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

Fecha: 21/11/2023.
Autores: Sergio López Fernández.
"""

print("Este programa genera 20 números aleatorios entre 0 y 100 y los almacena en un array de NumPy.")
print("El programa pasa todos los números pares a las primeras posiciones del array y todos los números impares"
      " a las celdas restantes.")
print("----------------------------------------------------------------------------------------------------------")

import numpy as np

TOTAL_NUMBERS = 20
MINIMUM_NUMBER = 0
MAXIMUM_NUMBER = 100

# Generamos una matriz de números aleatorios
numbers = np.random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1, TOTAL_NUMBERS)
print("Lista original:", numbers)

# Filtramos los números pares e impares usando NumPy
pair_num = numbers[numbers % 2 == 0]
odd_num = numbers[numbers % 2 != 0]

# Concatenamos las listas y mostramos el resultado
numbers = np.concatenate((pair_num, odd_num))
print("Lista ordenada:", numbers)
