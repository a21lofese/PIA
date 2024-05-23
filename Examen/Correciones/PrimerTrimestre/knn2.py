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
    k = 3

    predicted_class = knn(test_point, TRAIN_DATA, k)
    print(f"La clase asignada al punto de prueba {test_point} es: {predicted_class}")

def euclidian_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def knn(point, train_data, k=3):
    # distances = [(euclidian_distance(point, p), c) for p, c in train_data]
    distances = []
    for p, c in train_data:
        distances.append((euclidian_distance(point, p), c))
    distances.sort()

    k_neighbors = distances[:k]  # k puntos más cercanos.
    # classes = [cls for _, cls in k_neighbors]
    classes = []
    for _, c in k_neighbors:
        classes.append(c)

    return mode(classes)

if __name__ == '__main__':
    main()
