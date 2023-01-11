# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
'''
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

import random
from decimal import Decimal

lst = [round(random.uniform(0, 9), 2) for _ in range(1, 6)]
print(lst)
fract_lst = []

for number in lst:    
    first = int(number)
    num = Decimal(str(number - first))
    second = num.quantize(Decimal("1.00"))
    if second != 0:
        fract_lst.append(second)

print(max(fract_lst) - min(fract_lst))