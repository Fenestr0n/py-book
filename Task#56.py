# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
'''
Пример:
k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''

from random import randint

k = int(input("Введите натуральную степень k: "))

abc = [randint(0, 100) for _ in range(0, k + 1)]
res = []
s = ""

for item in range(len(abc) - 1, -1, -1):
    if abc[item] != 0:
        if item == 0:
            res.append(f"{abc[item]}")
        elif item == 1:
            if abc[item] != 1:
                res.append(f"{abc[item]}*x")
            else:
                res.append("x")
        else:
            if abc[item] != 1:
                res.append(f"{abc[item]}*x^{item}")
            else:
                res.append(f"x^{item}")
            
with open("file.txt", "w") as file:
    for i in range(0, len(res) - 1):
        s += f"{res[i]} + "
    s += f"{res[-1]} = 0"
    file.write(s)

print(s)