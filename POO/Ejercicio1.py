"""
Enunciado:
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer
 una nueva que se llamará Duration. Debe permitir:

Crear duraciones de tiempos.
Ejemplo: t = Duration(10,20,56)
Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
Las duraciones de tiempo se pueden comparar.
A las duraciones de tiempo les puedo sumar y restar segundos.
Las duraciones de tiempo se pueden sumar y restar.

Fecha: 28/11/2023.
Autores: Sergio López Fernández.
"""


class Duration:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        self.normalize()

    def normalize(self):
        self.m += self.s // 60
        self.s = self.s % 60
        self.h += self.m // 60
        self.m = self.m % 60

    def __str__(self):
        # Formateo de salida para que siempre tenga dos dígitos
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    # Comparación
    def __eq__(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

    def __lt__(self, other):
        return self.h < other.h or (self.h == other.h and self.m < other.m) or (self.h == other.h and self.m == other.m and self.s < other.s)

    def __gt__(self, other):
        return self.h > other.h or (self.h == other.h and self.m > other.m) or (self.h == other.h and self.m == other.m and self.s > other.s)

    def __le__(self, other):
        return self.h <= other.h or (self.h == other.h and self.m <= other.m) or (self.h == other.h and self.m == other.m and self.s <= other.s)

    def __ge__(self, other):
        return self.h >= other.h or (self.h == other.h and self.m >= other.m) or (self.h == other.h and self.m == other.m and self.s >= other.s)

    def __ne__(self, other):
        return self.h != other.h or self.m != other.m or self.s != other.s

    # Operaciones de Durations
    def __add__(self, other):
        return Duration(self.h + other.h, self.m + other.m, self.s + other.s)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Duration(self.h - other.h, self.m - other.m, self.s - other.s)

    def __rsub__(self, other):
        return self.__sub__(other)

    # Operaciones de segundos
    def __add__(self, other):
        return Duration(self.h, self.m, self.s + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Duration(self.h, self.m, self.s - other)

    def __rsub__(self, other):
        return self.__sub__(other)
