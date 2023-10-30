"""
Enunciado:
Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no
se puedan ejecutar el resto de las opciones.

Fecha: 30/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa pide dos valores (a y b) y a continuación muestra un menú con diferentes opciones")
print("-----------------------------------------------------------------------------------------------")


def main():
    a, b = 0, 0
    values_asked = False
    while True:
        option = option_value()
        if option == 1:
            a, b = ask_values()
            values_asked = True
        elif option == 6:
            break
        elif not values_asked:
            print("No se han introducido los valores de A y B, por favor, introdúzcalos desde la opción 1.")
        elif option == 2:
            addition(a, b)
        elif option == 3:
            subtraction(a, b)
        elif option == 4:
            multiplication(a, b)
        elif option == 5:
            division(a, b)
        else:
            print("La opción introducida no es correcta, por favor, introduzca una opción válida.")
    print("Fin del programa.")


def option_value():
    print("\nMenú")
    print("----")
    print("1. Introducir valores A y B")
    print("2. Sumar los valores A y B")
    print("3. Restar los valores A y B")
    print("4. Multiplicar los valores A y B")
    print("5. Dividir los valores A y B")
    print("6. Terminar el programa")
    option = int(input("\nIntroduzca una opción: "))
    print()
    return option


def ask_values():
    a = int(input("Introduce el valor de A: "))
    b = int(input("Introduce el valor de B: "))
    return a, b


def addition(n1, n2):
    print(f"La suma de {n1} y {n2} es {n1 + n2}")


def subtraction(n1, n2):
    print(f"La resta de {n1} y {n2} es {n1 - n2}")


def multiplication(n1, n2):
    print(f"La multiplicación de {n1} y {n2} es {n1 * n2}")


def division(n1, n2):
    if n2 != 0:
        print(f"La división de {n1} y {n2} es {n1 / n2}")
    else:
        print("ERROR. No se puede dividir por 0.")


if __name__ == "__main__":
    main()
