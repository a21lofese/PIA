"""
Enunciado:
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

import time

print("Este programa muestra un cronómetro.")

# Inicializamos las variables
hours = 0
minutes = 0
seconds = 0

while True:
    print("Cronómetro")
    print("----------")
    print(f"{hours} : {minutes} : {seconds}")
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    time.sleep(1)
    print("\n" * 100)
