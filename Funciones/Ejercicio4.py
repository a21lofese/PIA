"""
Enunciado:
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres.

Por ejemplo, el 213 es él ..___ .____ ...__ en Morse. Utiliza esta función en un programa
para comprobar que funciona bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Fecha: 30/10/2023.
Autores: Sergio López Fernández.
"""

MINUS = "-....-"
DECIMAL_POINT = ".-.-.-"
DIGITS = ["-----", ".-----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
SEPARATOR = " "


def convert_to_morse(number):
    """
    Convert a number to morse code.
    :param number: Number to convert.
    :return: Morse code.
    """
    morse = ""
    for digit in str(number):
        morse += DIGITS[int(digit)] + SEPARATOR
    return morse[:-1]


if __name__ == "__main__":
    print(convert_to_morse(213))
    print(convert_to_morse(1234567890))
    print(convert_to_morse(0))
    print(convert_to_morse(1))
    print(convert_to_morse(12))
    print(convert_to_morse(34))

