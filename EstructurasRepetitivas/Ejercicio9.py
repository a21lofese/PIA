"""
Enunciado:
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella
que se lee igual adelante que atrás. No se pueden usar slices.

Fecha: 23/10/2023.
Autores: Sergio López Fernández.
"""

print("Este programa indica si una palabra es palíndroma o no.")
print("-------------------------------------------------------")

# Inicializamos las variables.
word = input("Introduce una palabra: ")
inverted_word = ""
is_palindrome = False

word = word.lower()
for i in range(len(word) - 1, -1, -1):
    inverted_word += word[i]

if word == inverted_word:
    is_palindrome = True

print(f"La palabra '{word}' es palíndroma") if is_palindrome else print(f"La palabra '{word}' no es palíndroma")
