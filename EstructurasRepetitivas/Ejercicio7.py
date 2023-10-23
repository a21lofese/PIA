"""
Enunciado:
Mostrar en pantalla los N primeros número primos.
Se pide por teclado la cantidad de números primos que queremos mostrar.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

import math

# Inicializamos las variables
count = 0
number = 2

print("Este programa muestra los N primeros números primos.")
print("----------------------------------------------------")

while True:
    numbers_to_show = int(input("Introduce la cantidad de números primos que quieres mostrar: "))
    if numbers_to_show > 0:
        break

print(f"Los {numbers_to_show} primeros números primos son: ")

while count < numbers_to_show:
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number) if count == numbers_to_show - 1 else print(number, end=", ")
        count += 1
    number += 1
