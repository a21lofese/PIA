"""
Enunciado:
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro
de otras si es necesario.

Observa bien lo que hace cada función, ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo.
Por ejemplo, la función is_palindromic() resulta trivial teniendo turn() y la función next_prime() también es muy
fácil de implementar teniendo is_prime().

Está prohibido usar funciones de conversión del número a una cadena.

- is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
- is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
- next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
- digits: devuelve el número de dígitos de un número entero.
- turn: le da la vuelta a un número.
- digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de
  izquierda a derecha.
- digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra,
  devuelve -1.
- remove_behind: le quita a un número n dígitos por detrás (por la derecha).
- remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
- paste_behind: añade un dígito a un número por detrás.
- paste_ahead: añade un dígito a un número por delante.
- piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
- put_numbers_together: pega dos números para formar uno.

Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.

Fecha: 30/10/2023.
Autores: Sergio López Fernández.
"""

def is_palindromic(number):
    """
    Función que comprueba si un número es capicúa.
    :param number: Número a comprobar.
    :return: True si es capicúa, False si no lo es.
    """
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


def is_prime(number):
    """
    Función que comprueba si un número es primo.
    :param number: Número a comprobar.
    :return: True si es primo, False si no lo es.
    """
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def next_prime(number):
    """
    Función que devuelve el menor primo que es mayor al número que se pasa como parámetro.
    :param number: Número a comprobar.
    :return: El menor primo que es mayor al número que se pasa como parámetro.
    """
    while True:
        number += 1
        if is_prime(number):
            return number


def digits(number):
    """
    Función que devuelve el número de dígitos de un número entero.
    :param number: Número a comprobar.
    :return: El número de dígitos de un número entero.
    """
    num = abs(number)
    digits_total = 1
    while num // 10 > 0:
        num /= 10
        digits_total += 1
    return digits_total


def turn(number):
    """
    Función que le da la vuelta a un número.
    :param number: Número a comprobar.
    :return: El número volteado.
    """
    num = abs(number)
    digits_total = digits(num)
    num_turned = 0
    for i in range(digits_total):
        num_turned += (num % 10) * (10 ** (digits_total - i - 1))
        num //= 10
    return num_turned


def digit_n(number, position):
    """
    Función que devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de
    izquierda a derecha.
    :param number: Número a comprobar.
    :param position: Posición del dígito.
    :return: El dígito que está en la posición n de un número entero.
    """
    num = abs(number)
    num = turn(num)
    for i in range(position):
        num //= 10
    return num % 10


def digit_position(number, digit):
    """
    Función que da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra,
    devuelve -1.
    :param number: Número a comprobar.
    :param digit: Dígito a buscar.
    :return: La posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra,
    devuelve -1.
    """
    num = abs(number)
    num = turn(num)
    position = 0
    while num > 0:
        if num % 10 == digit:
            return position
        else:
            num //= 10
            position += 1
    return -1


def remove_behind(number, digits_to_remove):
    """
    Función que le quita a un número n dígitos por delante (por la izquierda).
    :param number: Número a comprobar.
    :param digits_to_remove: Dígitos a quitar.
    :return: El número sin los dígitos quitados.
    """
    num = abs(number)
    num = turn(num)
    num = remove_ahead(num, digits_to_remove)
    return turn(num)


def remove_ahead(number, digits_to_remove):
    """
    Función que le quita a un número n dígitos por detrás (por la derecha).
    :param number: Número a comprobar.
    :param digits_to_remove: Dígitos a quitar.
    :return: El número sin los dígitos quitados.
    """
    num = abs(number)
    num = turn(num)
    for i in range(digits_to_remove):
        num //= 10
    return turn(num)


def paste_behind(number, digit):
    """
    Función que añade un dígito a un número por detrás.
    :param number: Número a comprobar.
    :param digit: Dígito a añadir.
    :return: El número con el dígito añadido.
    """
    num = abs(number)
    num = turn(num)
    num += digit * (10 ** digits(num))
    return turn(num)


def paste_ahead(number, digit):
    """
    Función que añade un dígito a un número por delante.
    :param number: Número a comprobar.
    :param digit: Dígito a añadir.
    :return: El número con el dígito añadido.
    """
    num = abs(number)
    num = turn(num)
    num = paste_behind(num, digit)
    return turn(num)


def piece_of_number(number, initial_position, final_position):
    """
    Función que toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
    correspondiente.
    :param number: Número a comprobar.
    :param initial_position: Posición inicial.
    :param final_position: Posición final.
    :return: El trozo correspondiente.
    """
    num = abs(number)
    num = turn(num)
    num = remove_behind(num, initial_position)
    num = remove_ahead(num, digits(num) - final_position - 1)
    return turn(num)


def put_numbers_together(number1, number2):
    """
    Función que pega dos números para formar uno.
    :param number1: Número 1.
    :param number2: Número 2.
    :return: Los dos números pegados.
    """
    num1 = abs(number1)
    num2 = abs(number2)
    num2 = turn(num2)
    num1 = paste_behind(num1, num2)
    return num1


def main():
    """
    Función principal.
    """
    print("¿Es capicúa el número 12321?:", is_palindromic(12321))
    print("¿Es primo el número 17?:", is_prime(17))
    print("¿Cuál es el siguiente primo de 17?:", next_prime(17))
    print("¿Cuántos dígitos tiene el número 12321?:", digits(12321))
    print("¿Cuál es el número volteado de 12321?:", turn(12321))
    print("¿Cuál es el dígito en la posición 3 del número 12321?:", digit_n(12321, 3))
    print("¿Cuál es la posición del dígito 2 en el número 12321?:", digit_position(12321, 2))
    print("¿Cuál es el número 12321 sin los 2 dígitos por detrás?:", remove_behind(12321, 2))
    print("¿Cuál es el número 12321 sin los 2 dígitos por delante?:", remove_ahead(12321, 2))
    print("¿Cuál es el número 12321 con el dígito 4 por detrás?:", paste_behind(12321, 4))
    print("¿Cuál es el número 12321 con el dígito 4 por delante?:", paste_ahead(12321, 4))
    print("¿Cuál es el trozo del número 12321 que va de la posición 1 a la 3?:", piece_of_number(12321, 1, 3))
    print("¿Cuál es el número que se forma al pegar el 12321 y el 456?:", put_numbers_together(12321, 456))


if __name__ == "__main__":
    main()
