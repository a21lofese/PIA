"""
Enunciado:
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €,
el tercero 40 € y así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total
de lo que pagará después de los 20 meses.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa calcula el total a pagar en 20 meses, pagando el doble cada mes.")
print("------------------------------------------------------------------------------")

# Inicializamos las variables.
MONTHS = 20
total = 0
pay = 10

for i in range(MONTHS):
    total += pay
    print(f"El mes {i + 1} se pagará {pay:,d}€.")
    pay *= 2

print(f"El total a pagar en 20 meses es de {total:,d}€.")
