# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
'''
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

from random import randint

n = int(input("Количество элементов списка: "))
lst = [randint(0, 9) for _ in range(1, n + 1)]
print(lst)

odd = [i for i in lst if lst.index(i) % 2 != 0]
print(f"На нечётных позициях элементы {odd}, ответ: {sum(odd)}")