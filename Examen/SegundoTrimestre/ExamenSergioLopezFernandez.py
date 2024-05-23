from stack import Stack
from menu import Menu
import pickle

stack = Stack()


def main():
    menu = Menu(
        "Crear una pila vacía.",
        "Crear una pila desde un fichero pickle.",
        "Introducir (apilar) un elemento en la pila.",
        "Sacar (desapilar) un elemento de la pila (debe indicarse su valor).",
        "Mostrar el elemento superior de la pila.",
        "Vaciar la pila.",
        "Mostrar la pila.",
        "Mostrar el número de elementos que tiene la pila.",
        "Duplicar la pila (hacemos uso del operador +).",
        "Quitar un elemento de la pila, si lo tiene (hacemos uso del operador -).",
        "Cambiar el tamaño máximo de la pila.",
        "Guardar la pila en un fichero pickle.",
        "Terminar"
    )

    while True:
        opc = menu.choose()
        match opc:
            case 1: new_empty_stack()
            case 2: load_stack()
            case 3: push_element()
            case 4: pop_element()
            case 5: top_element()
            case 6: clear_stack()
            case 7: show_stack()
            case 8: show_length()
            case 9: duplicate()
            case 10: remove_element()
            case 11: change_size()
            case 12: save_stack()
            case _:
                break
    print("Hasta la próxima! :-)")


def new_empty_stack():
    Stack()


def load_stack():
    try:
        url = input("Introduce la url del archivo: ")
        if not isinstance(url, str):
            raise ValueError("La url debe ser una cadena.")
        stack = pickle.load(open(f'{url}', 'rb'))
    except ValueError:
        print("La url debe ser una cadena.")


def push_element():
    try:
        element = int(input("Introduce el elemento que quiere añadir a la pila: "))
        if not isinstance(element, int):
            raise ValueError("El elemento que quiere añadir no es un número entero.")
        stack.push(element)
    except ValueError:
        print("Debe introducir un valor entero.")
    except MemoryError:
        print("La pila esta llena, no puede añadir más elementos.")


def pop_element():
    try:
        print(f"Ha sacado el elemento: {stack.pop()}")
    except MemoryError:
        print("No es posible extraer más elementos de la pila.")


def top_element():
    try:
        print(f"El elemento superior de la pila es: {stack.top()}")
    except MemoryError:
        print("No es posible mostrar el elemento superior de la pila.")


def clear_stack():
    stack.clear_out()


def show_stack():
    print(stack)


def show_length():
    print(f"La pila tiene {stack.length()} elementos.")


def duplicate():
    try:
        stack + stack
    except MemoryError:
        print("La pila excede el tamaño máximo.")


def remove_element():
    try:
        element = int(input("Introduce el elemento a eliminar: "))
        if not isinstance(element, int):
            raise ValueError("El elemento que quiere eliminar no es un número entero.")
        stack - element
    except ValueError:
        print("Debe introducir un valor entero.")


def change_size():
    try:
        element = int(input("Introduce el nuevo tamaño: "))
        if not isinstance(element, int):
            raise ValueError("El tamaño introducido no es un número entero.")
        stack.SIZE = element
    except ValueError:
        print("Debe introducir un valor entero.")


def save_stack():
    pickle.dump(stack, open('stack.pkl', 'wb'))
    print("Pila almacenada.")


if __name__ == "__main__":
    main()
