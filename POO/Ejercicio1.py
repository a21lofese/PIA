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
        self.__h, self.__m, self.__s = h, m, s
        self.__normalize()

    def __normalize(self):
        self.m += self.s // 60
        self.s = self.s % 60
        self.h += self.m // 60
        self.m = self.m % 60

    def to_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, m):
        self.__m = m

    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, s):
        self.__s = s

    def __str__(self):
        return f"{self.h}:{self.m:02}:{self.s:02}"

    # Comparación
    def __eq__(self, other: 'Duration'):
        return self.to_seconds() == other.to_seconds()

    def __lt__(self, other: 'Duration'):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other: 'Duration'):
        return self.to_seconds() > other.to_seconds()

    def __le__(self, other: 'Duration'):
        return self.to_seconds() <= other.to_seconds()

    def __ge__(self, other: 'Duration'):
        return self.to_seconds() >= other.to_seconds()

    def __ne__(self, other: 'Duration'):
        return self.to_seconds() != other.to_seconds()

    # Operaciones de Durations
    def __add__(self, other):
        if isinstance(other, Duration):
            return Duration(self.h + other.h, self.m + other.m, self.s + other.s)
        elif isinstance(other, int):
            return Duration(self.h, self.m, self.s + other)
        else:
            raise TypeError("Tipo de dato no soportado")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Duration):
            return Duration(self.h - other.h, self.m - other.m, self.s - other.s)
        elif isinstance(other, int):
            return Duration(self.h, self.m, self.s - other)
        else:
            raise TypeError("Tipo de dato no soportado")

    def __rsub__(self, other):
        return self.__sub__(other)
