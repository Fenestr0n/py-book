# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    try:
        num = int(input("Введите номер четверти: "))
        if num == 1:
            print("x ≥ 0 и y ≥ 0")
        elif num == 2:
            print("x ≤ 0 и y ≥ 0")
        elif num == 3:
            print("x ≤ 0 и y ≤ 0")
        elif num == 4:
            print("x ≥ 0 и y ≤ 0")
        else:
            continue
        break
    except ValueError:
        continue