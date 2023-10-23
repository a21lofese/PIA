"""
Enunciado:
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

print("Programa que imprime todos los números pares entre dos números que se le pidan al usuario.")

# Declaramos las variables
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Si el primer número es mayor que el segundo, los intercambiamos
if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)
