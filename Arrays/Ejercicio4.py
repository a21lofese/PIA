"""
Enunciado:
Escribe un programa que lea 5 números por teclado y que los almacene en una lista. Rota los elementos de esa lista, es
decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra en
la última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.

Fecha: 21/11/2023.
Autores: Sergio López Fernández.
"""

print("Este programa rota los elementos de una lista.")
print("----------------------------------------------")

TOTAL_NUM = 5
numbers_list = []

print("Introduce números enteros:")
for i in range(TOTAL_NUM):
    numbers_list.append(int(input()))

print("Lista original:", numbers_list)

last_number = numbers_list[TOTAL_NUM - 1]
for i in range(TOTAL_NUM - 1, 0, -1):
    numbers_list[i] = numbers_list[i - 1]
numbers_list[0] = last_number

print("Lista rotada:", numbers_list)
