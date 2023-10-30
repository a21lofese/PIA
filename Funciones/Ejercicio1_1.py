"""
Enunciado:
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra
el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se volverá
a mostrar, a menos que no se dé a la opción terminar.

Fecha: 30/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa pide dos valores (a y b) y a continuación muestra un menú con diferentes opciones")
print("-----------------------------------------------------------------------------------------------")


def main():
    a = int(input("Introduce el valor de A: "))
    b = int(input("Introduce el valor de B: "))
    while True:
        option = option_value()
        if option == 1:
            addition(a, b)
        elif option == 2:
            subtraction(a, b)
        elif option == 3:
            multiplication(a, b)
        elif option == 4:
            division(a, b)
        elif option == 5:
            break
        else:
            print("La opción introducida no es correcta, por favor, introduzca una opción válida.")
    print("Fin del programa.")


def option_value():
    print("\nMenú")
    print("----")
    print("1. Sumar los valores A y B")
    print("2. Restar los valores A y B")
    print("3. Multiplicar los valores A y B")
    print("4. Dividir los valores A y B")
    print("5. Terminar el programa")
    option = int(input("\nIntroduzca una opción: "))
    print()
    return option


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


# Esto es para que el programa no se ejecute si se importa como módulo.
# Si se ejecuta como programa principal, se ejecuta la función main().
if __name__ == "__main__":
    main()
