"""
Enunciado:
Hacer un programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización
después de que se pida al usuario/a:

- Importe del préstamo.
- La tasa de interés anual.
- Y el plazo de pago en años.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

import math

print("Este programa calcula la cuota de una hipoteca y su tabla de amortización.")
print("--------------------------------------------------------------------------")

# Declaramos las variables.
bank_loan = float(input("Introduzca el importe del préstamo: "))
interest_rate = float(input("Introduzca la tasa de interés anual: "))
years = int(input("Introduzca el plazo de pago en años: "))

# Constantes.
MONTHS = 12
INTEREST_RATE = interest_rate / 100
MONTHLY_INTEREST_RATE = INTEREST_RATE / MONTHS
MONTHS_TO_PAY = years * MONTHS

# Calculamos la cuota.
monthly_fee = bank_loan * (MONTHLY_INTEREST_RATE / (1 - math.pow((1 + MONTHLY_INTEREST_RATE), -MONTHS_TO_PAY)))

# Mostramos la cuota.
print("La cuota mensual es de: ", round(monthly_fee, 2), "€")

# Calculamos la tabla de amortización.
print("Tabla de amortización:")
print("Mes\tCuota\tInterés\tAmortización\tCapital pendiente")
for i in range(1, MONTHS_TO_PAY + 1):
    interest = bank_loan * MONTHLY_INTEREST_RATE
    amortization = monthly_fee - interest
    bank_loan = bank_loan - amortization
    print(f"{i}\t{monthly_fee:.2f}€\t{interest:.2f}€\t{amortization:.2f}€\t\t\t{bank_loan:.2f}€")