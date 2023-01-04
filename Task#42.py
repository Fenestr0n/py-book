# Напишите программу, которая принимает на вход НАТУРАЛЬНОЕ число и показывает сумму его цифр.
'''
Пример:
6782 -> 23
56 -> 11
67 -> 13
19845 -> 27
'''


def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    # print(total)
    return total


assert sum_of_digits(6782) == 23
assert sum_of_digits(56) == 11
assert sum_of_digits(67) == 13
assert sum_of_digits(19845) == 27
