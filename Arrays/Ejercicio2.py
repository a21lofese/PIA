"""
Enunciado:
Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

Fecha: 21/11/2023.
Autores: Sergio López Fernández.
"""

import numpy as np

print("Este programa muestra el contenido de tres listas, number, square y cube, con 20 números enteros cada una.")
print("----------------------------------------------------------------------------------------------------------")

MINIMUM_VALUE = 0
MAXIMUM_VALUE = 100
ARRAY_LENGTH = 20

number = np.random.randint(MINIMUM_VALUE, MAXIMUM_VALUE + 1, ARRAY_LENGTH)
square = np.square(number)
cube = np.power(number, 3)

print("number\t\tsquare\t\tcube")
print("-----------------------------")
for i in range(ARRAY_LENGTH):
    print(f"{number[i]:4} {square[i]:12} {cube[i]:10}")
    print("-----------------------------")

"""
Conclusiones:
    - El uso de numpy es más sencillo que el uso de listas.
    - La generación de números aleatorios es más sencilla con numpy.
    - Y su sintaxis es más sencilla y legible.
"""