# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
'''
Пример:
Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
Сумма 9.06
'''

num = int(input("Введите число: "))
lst = [n for n in range(1, num + 1)]
tmp = list(map(lambda n: (1 + 1/n) ** n, lst))
res = sum(tmp)

print(tmp)  # [2.0, 2.25, 2.37037037037037, 2.44140625]
print(res)  # 9.06177662037037