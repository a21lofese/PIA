"""
Queremos hacer una aplicación que pida un personaje de Star Wars y nos diga los nombres de las películas en las que ha
salido y su planeta de nacimiento, para ello haz uso de esta API.
"""

import requests


def get_all_names():
    names = []

    url_character = "https://swapi.dev/api/people/"
    while url_character:
        try:
            response_character = requests.get(url_character)
            response_character.raise_for_status()  # Manejo de errores HTTP

            datos_personajes = response_character.json()
            names.extend([character['name'] for character in datos_personajes['results']])
            url_character = datos_personajes['next']

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la API: {e}")
            break

    return names


def show_names():
    names = get_all_names()

    print("Nombres de personajes disponibles:")
    for i, character_name in enumerate(names, 1):
        print(f"{i}. {character_name}")
    print("\n")


def get_info_of(character_name):
    url_personajes = "https://swapi.dev/api/people/"
    params = {'search': character_name}

    try:
        response_character = requests.get(url_personajes, params=params)
        response_character.raise_for_status()

        character_data = response_character.json()

        if character_data['count'] == 0:
            print("Personaje no encontrado.")
            return

        character = character_data['results'][0]
        character_name = character['name']
        films = [requests.get(pelicula).json()['title'] for pelicula in character['films']]
        url_homeworld = character['homeworld']
        homeworld = requests.get(url_homeworld).json()['name']

        print(f"Información de {character_name}:")
        print(f"Películas: {', '.join(films)}")
        print(f"Planeta de nacimiento: {homeworld}")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener información del personaje: {e}")


if __name__ == "__main__":
    show_names()

    character_name = input("Introduce el nombre de un personaje de Star Wars: ")
    get_info_of(character_name)
