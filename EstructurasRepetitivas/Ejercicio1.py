"""
Enunciado:
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa pide números y te dice cuantos son positivos, negativos o ceros.")

# Inicializamos las variables
positive = 0
negative = 0
zero = 0

numbers = int(input("Introduce la cantidad de números a introducir: "))
while numbers <= 0:
    print("La cantidad de números a introducir debe ser mayor que 0.")
    numbers = int(input("Introduce la cantidad de números a introducir: "))

# Pedimos los números
for i in range(numbers):
    number = int(input("Introduce un número: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print(f"Has introducido {positive} número/s positivos, {negative} números negativo/s y {zero} ceros.")
