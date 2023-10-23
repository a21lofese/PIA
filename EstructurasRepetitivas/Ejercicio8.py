"""
Enunciado:
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
No se pueden usar los métodos de Python para este fin ni slices.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa comprueba si una cadena contiene una subcadena.")
print("-------------------------------------------------------------")

# Inicializamos las variables.
string = input("Introduce una cadena: ")
substring = input("Introduce una subcadena: ")
found = False

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        found = True
        break

print("La subcadena se encuentra en la cadena.") if found else print("La subcadena no se encuentra en la cadena.")
