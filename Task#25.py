# Проверить, является ли введенный список симметричным.
a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a[i] != a[len(a) - 1 - i]:
        print("Список не симметричный")
        break
    if i == len(a) - 1:
        print("Список симметричный")