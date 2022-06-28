# Вывести фрагмент таблицы умножения
a = int(input("> "))
b = int(input("> "))
c = int(input("> "))
d = int(input("> "))
for i in range(c, d + 1):
    print("\t", " " + str(i), end=" ")
print()
for i in range(a, b + 1):
    print(i, "", "\t", end=" ")
    for j in range(c, d + 1):
        print(i * j, " ", end="\t")
        if j == d:
            print()