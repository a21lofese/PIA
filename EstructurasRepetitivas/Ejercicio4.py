"""
Enunciado:
Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el
superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las
siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa pide un intervalo y una serie de números, y te dice cuantos números están dentro del intervalo,"
      "cuantos están fuera y si has introducido algún número igual a los límites del intervalo.")
print("---------------------------------------------------------------------------------------------------------------")

# Declaración de variables.
NUMBER_TO_EXIT = 0
lower_limit = int(input("Introduce el límite inferior del intervalo: "))
upper_limit = int(input("Introduce el límite superior del intervalo: "))
added_numbers = 0
numbers_outside = 0
equal_numbers = False

# Bucle que se repite hasta que el límite inferior sea menor que el superior.
while lower_limit > upper_limit:
    print("El límite inferior no puede ser mayor que el superior.")
    lower_limit = int(input("Introduce el límite inferior del intervalo: "))
    upper_limit = int(input("Introduce el límite superior del intervalo: "))

# Bucle que se repite hasta que el usuario introduzca el número 0.
number = int(input("Introduce un número: "))
while number != NUMBER_TO_EXIT:
    if lower_limit < number < upper_limit:
        added_numbers += number
    elif number == lower_limit or number == upper_limit:
        equal_numbers = True
    else:
        numbers_outside += 1
    number = int(input("Introduce un número: "))

print(f"La suma de los números que están dentro del intervalo es: {added_numbers}")
print(f"La cantidad de números que están fuera del intervalo es: {numbers_outside}")
print("Has introducido algún número igual a los límites del intervalo.") if equal_numbers\
      else print("No has introducido ningún número igual a los límites del intervalo.")
