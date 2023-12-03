"""
Enunciado:
En Python podemos manejar fechas, pero no nos gusta, vamos a crear una clase Date. Debe permitir:

Crear fechas.
Ejemplo: f = Date(17, 11, 2022)

Estas fechas son erróneas:
    Date(78, -45, 0)
    Date(31, 6, 2022)
    Date(29, 2, 2022)

Las fechas se pueden comparar.
A las fechas se le pueden sumar y restar días.
Las fechas se pueden restar.
Se debe poder averiguar el día de la semana de una fecha.

Fecha: 28/11/2023.
Autores: Sergio López Fernández.
"""


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.validate_date()

    def validate_date(self):
        if not (1 <= self.day <= 31):
            raise ValueError("El día introducido no es válido.")
        if not (1 <= self.month <= 12):
            raise ValueError("El mes introducido no es válido.")
        if self.year < 0:
            raise ValueError("El año introducido no es válido.")

        days_in_month = {
            1: 31, 2: 29 if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0) else 28,
            3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        if not (1 <= self.day <= days_in_month[self.month]):
            raise ValueError("El día introducido no es válido.")

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __gt__(self, other):
        if self.year != other.year:
            return self.year > other.year
        elif self.month != other.month:
            return self.month > other.month
        else:
            return self.day > other.day

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        elif self.month != other.month:
            return self.month < other.month
        else:
            return self.day < other.day

    def __add__(self, days):
        new_day = self.day + days
        return self._normalize_date(new_day, self.month, self.year)

    def __radd__(self, days):
        return self.__add__(days)

    def __sub__(self, days):
        new_day = self.day - days
        return self._normalize_date(new_day, self.month, self.year)

    def __rsub__(self, days):
        return self.__sub__(days)

    def _normalize_date(self, day, month, year):
        days_in_month = {
            1: 31, 2: 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
            3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        while day <= 0:
            if month == 1:
                year -= 1
                month = 12
            else:
                month -= 1
                day += days_in_month[month]

        while day > days_in_month[month]:
            day -= days_in_month[month]
            if month == 12:
                year += 1
                month = 1
            else:
                month += 1

        return Date(day, month, year)

    def day_of_week(self):
        days_of_week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        day = self.day
        month = self.month
        year = self.year

        if month < 3:
            month += 12
            year -= 1

        K = year % 100
        J = year // 100

        day_of_week_index = (day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7

        return days_of_week[day_of_week_index]


# Ejemplos de uso
fecha1 = Date(17, 11, 2022)
fecha2 = Date(17, 11, 2022)
fecha3 = Date(18, 11, 2022)

print(fecha1)  # Imprime: 17/11/2022
print(fecha1 == fecha2)  # Imprime: True
print(fecha1 < fecha3)  # Imprime: True
print(fecha1 + 5)  # Imprime: 22/11/2022
print(fecha1 - 5)  # Imprime: 12/11/2022
print(fecha1.day_of_week())  # Imprime el día de la semana
