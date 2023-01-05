# Напишите программу, которая принимает на вход ВЕЩЕСТВЕННОЕ число и показывает сумму его цифр.
'''
Пример:
6782 -> 23
0.56 -> 11
0.67 -> 13
198.45 -> 27
'''


def sum_of_digits(number):
    total = sum(int(i) for i in str(number) if i.isdigit())
    # print(total)
    return total


assert sum_of_digits(6782) == 23
assert sum_of_digits(0.56) == 11
assert sum_of_digits(0.67) == 13
assert sum_of_digits(198.45) == 27
