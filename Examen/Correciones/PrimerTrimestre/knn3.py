"""
Ejercicio anterior con código más algorítmico.
"""

from math import sqrt
from statistics import mode

TRAIN_DATA = [
        ((2, 3), 1),
        ((4, 2), 1),
        ((3, 5), 2),
        ((6, 3), 2),
        ((5, 1), 1)
    ]
def main():
    test_point = (4, 4)
    radius = 5

    predicted_class = knn(test_point, TRAIN_DATA, radius)
    print(f"La clase asignada al punto de prueba {test_point} es: {predicted_class}")

def euclidian_distance(point1, point2):  # bonus 1
    if len(point1) != len(point2):
        raise TypeError("Los puntos no tienen las mismas dimensiones")
    quadratic_sum = 0
    for i in len(point1):
        quadratic_sum += (point1[i] - point2[i]) ** 2
    return sqrt(quadratic_sum)

def knn(point, train_data, radius):  # bonus 2
    classes = []
    for p, c in train_data:
        d = euclidian_distance(point, p)
        if d <= radius:
            classes.append(c)

    return mode(classes)

if __name__ == '__main__':
    main()
