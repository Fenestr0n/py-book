# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
'''
x = 34; y = -30 -> 4
x = 2; y = 4 -> 1
x = -34; y = -30 -> 3
'''	

while True:
    try:
        x = float(input("Введите координату X = "))
    except ValueError:
        x = 0
    if x != 0:
        while True:
            try:
                y = float(input("Введите координату Y = "))
            except ValueError:
                y = 0
            if y != 0:
                break
        break


if x > 0 and y > 0:
    print("I четверть плоскости")
elif x < 0 and y > 0:
    print("II четверть плоскости")
elif x < 0 and y < 0:
    print("III четверть плоскости")
elif x > 0 and y < 0:
    print("IV четверть плоскости")
