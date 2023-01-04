# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
'''
A (3, 6); B (2, 1) -> 5.09
A (7, -5); B (1, -1) -> 7.21
'''


def distance(a, b):
    dist = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return int(dist * 100) / 100


while True:
    try:
        a = [float(i) for i in input("Введите координаты точки A через запятую (x, y): ").split(",")]
        b = [float(i) for i in input("Введите координаты точки B через запятую (x, y): ").split(",")]
        print(distance(a, b))
        break
    except ValueError:
        continue
