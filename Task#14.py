# Определить четверть на координатной плоскости в которой лежит введенная точка.
x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")
else:
    print("Нет данных")
