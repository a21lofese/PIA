"""
2.- El FBI tiene recorte de personal informático y solicitan nuestra ayuda, quieren saber cuantos fugitivos tienes
registrados en cada una de sus oficinas, para ello han habilitado una API a la que puedes acceder desde aquí.

El programa debe mostrar el nombre de cada oficina (ordenado) y la cantidad de fugitivos registrados. También debe
mostrar la cantidad de fugitivos no registrados en ninguna oficina.

Ten en cuenta que cada consulta muestra un número limitado de registros, vas a tener que hacer consultas iterativas
enviando como parámetro la página de la consulta hasta que ya no queden páginas que consultar.
"""

import requests
import json


def main():
    fugitivos_por_oficina = {}
    fugitivos_no_registrados = 0
    pagina = 1

    while True:
        response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': pagina})

        if response.status_code != 200:
            print(f"Error en la solicitud a la API. Código de estado: {response.status_code}")
            break

        data = json.loads(response.content)

        if 'items' not in data or not data['items']:
            break

        for fugitivo in data['items']:
            oficinas = fugitivo.get('field_offices', [])

            if not oficinas:
                fugitivos_no_registrados += 1
            else:
                for oficina in oficinas:
                    if oficina in fugitivos_por_oficina:
                        fugitivos_por_oficina[oficina] += 1
                    else:
                        fugitivos_por_oficina[oficina] = 1

        pagina += 1

    oficinas_ordenadas = sorted(fugitivos_por_oficina.items(), key=lambda x: x[0])

    print("Cantidad de fugitivos por oficina:")
    for oficina, cantidad in oficinas_ordenadas:
        print(f"{oficina}: {cantidad}")

    print("\nCantidad de fugitivos no registrados en ninguna oficina:", fugitivos_no_registrados)


if __name__ == "__main__":
    main()
