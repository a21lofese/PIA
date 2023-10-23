"""
Enunciado:
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el
número (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número
que había generado.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

import random

# Declaramos las variables
random_number = random.randint(1, 100)
chances = 10

print("Adivina el número que estoy pensando del 1 al 100. Tienes 10 intentos.")
while chances > 0:
    user_number = int(input("Introduce un número: "))
    if user_number == random_number:
        print(f"Has acertado en {10 - chances + 1} intentos.")
        break
    elif user_number < random_number:
        print("El número que estoy pensando es mayor que el que has introducido.")
    else:
        print("El número que estoy pensando es menor que el que has introducido.")
    chances -= 1
    print(f"Te quedan {chances} intentos.")
else:
    print(f"Has perdido. El número que estaba pensando era el {random_number}.")
