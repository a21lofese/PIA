"""
Enunciado:
Crea una clase, y pruébala, que modele fracciones. Debe permitir:
Crear fracciones indicando numerador y denominador.
Ejemplo: f = Fraction(2, 3)
No se puede tener un denominador cero.
Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Esto se puede hacer: f + 1, 5 * f
Las fracciones se pueden comparar.
==, <, <=, >, >=, !=
Estas dos fracciones son iguales: 1/2 y 2/4
Esto se puede hacer 1 < 1/2

Fecha: 28/11/2023.
Autores: Sergio López Fernández.
"""

import math


class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("El denominador no puede ser 0")
        maximum_common_divisor = math.gcd(numerator, denominator)
        self.numerator = numerator // maximum_common_divisor
        self.denominator = denominator // maximum_common_divisor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Operaciones con dos fracciones
    def __add__(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __radd__(self, other: 'Fraction'):
        return self.__add__(other)

    def __sub__(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __rsub__(self, other: 'Fraction'):
        return self.__sub__(other)

    def __mul__(self, other: 'Fraction'):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rmul__(self, other: 'Fraction'):
        return self.__mul__(other)

    def __truediv__(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __rtruediv__(self, other: 'Fraction'):
        return self.__truediv__(other)

    # Operaciones con un número

    def __add__(self, other: int):
        return Fraction(self.numerator + other * self.denominator, self.denominator)

    def __radd__(self, other: int):
        return self.__add__(other)

    def __sub__(self, other: int):
        return Fraction(self.numerator - other * self.denominator, self.denominator)

    def __rsub__(self, other: int):
        return self.__sub__(other)

    def __mul__(self, other: int):
        return Fraction(self.numerator * other, self.denominator)

    def __rmul__(self, other: int):
        return self.__mul__(other)

    def __truediv__(self, other: int):
        return Fraction(self.numerator, self.denominator * other)

    def __rtruediv__(self, other: int):
        return self.__truediv__(other)

    # Operaciones de comparación

    def __eq__(self, other: 'Fraction'):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __eq__(self, other: int):
        return self.numerator == other and self.denominator == 1

    def __ne__(self, other: 'Fraction'):
        return not self.__eq__(other)

    def __ne__(self, other: int):
        return not self.__eq__(other)

    def __lt__(self, other: 'Fraction'):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __lt__(self, other: int):
        return self.numerator < other * self.denominator

    def __le__(self, other: 'Fraction'):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __le__(self, other: int):
        return self.numerator <= other * self.denominator

    def __gt__(self, other: 'Fraction'):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __gt__(self, other: int):
        return self.numerator > other * self.denominator

    def __ge__(self, other: 'Fraction'):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __ge__(self, other: int):
        return self.numerator >= other * self.denominator
