# Пользователь вводит тип фигуры, и программа считает ее площадь.
# треугольник прямоугольник круг
typeFigure = input("Введите тип фигуры: ")

if typeFigure == "треугольник":
    a = int(input("a >>> "))
    b = int(input("b >>> "))
    c = int(input("c >>> "))
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif typeFigure == "прямоугольник":
    a = int(input("a >>> "))
    b = int(input("b >>> "))
    print(a * b)
elif typeFigure == "круг":
    r = int(input("r >>> "))
    print(3.1415 * r ** 2)
else:
    print("Неизвестный тип")