"""
Enunciado:
Dado un conjunto de datos de entrenamiento en dos dimensiones y un punto de prueba, implementa
el algoritmo k-NN para clasificar el punto de prueba. Utiliza la distancia euclídea como medida de
similitud, pesos uniformes y considera un valor de k igual a 3.
Los datos de entrenamiento son:
Punto A: (2, 3), Clase: 1
Punto B: (4, 2), Clase: 1
Punto C: (3, 5), Clase: 2
Punto D: (6, 3), Clase: 2
Punto E: (5, 1), Clase: 1
Pasos a seguir:
    • Calcula la distancia euclídea entre el punto que hay que clasificar y cada punto de
    entrenamiento.
    • Selecciona los k puntos más cercanos.
    • Determina la clase mayoritaria entre los k vecinos más cercanos.
    • Asigna la clase predicha al punto.
Crea una función para la distancia euclídea pasándoles dos puntos (dos tuplas) y otra para
determinar la clase mayoritaria pasándole el punto a predecir, el conjunto de entrenamiento y k (por
defecto 3).
La fórmula de la distancia euclidiana entre dos puntos (x1, y1) y (x2, y2) en un plano bidimensional
es dada por el teorema de Pitágoras:
√(x2−x1)^2+(y2−y1)^2
Pruébalo con el punto (4, 4).

Realizado por: Sergio López Fernández
Fecha: 13/12/2023
"""

import math
import statistics as st

print("----------------------------------------------------")
print("Clasificación del Punto (4, 4) con el algorítmo k-NN")
print("----------------------------------------------------")

# Clases
CLASS = [1, 2]

# Conjunto de entrenamiento
POINTS = [
    [(2, 3), CLASS[0]],
    [(4, 2), CLASS[0]],
    [(3, 5), CLASS[1]],
    [(6, 3), CLASS[1]],
    [(5, 1), CLASS[0]]
]

# Punto a clasificar
POINT = (4, 4)


def euclidean_distance(point1, point2):
    """
    Calcula la distancia euclídea entre dos puntos.
    :param point1: Coordenadas del primer punto.
    :param point2: Coordenadas del segundo punto.
    :return: Devuelve la distancia entre los puntos.
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def majority_class(point_to_classify, training_set, k=3):
    """
    Devuelve la clase a la que pertenece un punto según unos datos de entrenamiento.
    :param point_to_classify: Punto del cual queremos saber a qué clase pertenece.
    :param training_set: Conjunto de puntos de entrenamiento.
    :param k: Distancia por defecto que usaremos para saber a qué grupo de vecinos pertenece el punto.
    :return: Devuelve la clase a la que pertenece el punto.
    """
    # Calculamos la distancia entre el punto a clasificar y el conjunto de entrenamiento
    euclidean_distance_list = []
    for point in training_set:
        euclidean_distance_list.append(euclidean_distance(point_to_classify, point[0]))

    # Obtener las clases de los puntos cercanos
    nearby_points_class = []
    counter = 0
    for distance in euclidean_distance_list:
        counter += 1
        if distance >= k:
            nearby_points_class.append(training_set[counter - 1][1])

    return st.mode(nearby_points_class)  # Devuelve la clase a través de la moda
    # return nearby_points_class # Devuelve las clases de los puntos cercanos


print(f"La clase del Punto {POINT} es: {majority_class(POINT, POINTS)}")
