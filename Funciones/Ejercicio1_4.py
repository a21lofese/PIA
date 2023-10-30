"""
Enunciado:
Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción
(por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función.

Fecha: 30/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa pide dos valores (a y b) y a continuación muestra un menú con diferentes opciones")
print("-----------------------------------------------------------------------------------------------")


def main():
    a, b = 0, 0
    values_asked = False
    while True:
        option = menu("Introducir valores A y B", "Sumar los valores A y B", "Restar los valores A y B",
                      "Multiplicar los valores A y B", "Dividir los valores A y B", "Terminar el programa")
        if option == 1:
            a, b = ask_values()
            values_asked = True
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
            break
    print("Fin del programa.")


def menu(*options):
    while True:
        print("\nMenú")
        print("----")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option = int(input("\nEscoja una opción: "))
        print()
        if 1 <= option <= len(options):
            return option
        print("La opción introducida no es correcta, por favor, introduzca una opción válida.")


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
