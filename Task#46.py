# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import math
from random import randint

n = int(input("Количество элементов списка: "))
lst = [randint(-n, n) for _ in range(1, n + 1)]
pos = {randint(1, n) for _ in range(1, n + 1)}

with open("file.txt", "w") as file:
    for item in pos:
        file.write(f"{str(item)}\n")

with open("file.txt", "r", encoding="utf8") as file:
    positions = file.readlines()

result = math.prod([lst[i-1] for i in [int(x) for x in positions]])

print(lst)
print(pos)
print(result)