# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов [Негафибоначчи].
'''
Пример:
Для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def nega_fibonacci(n):
    if n in (1, 2):
        return 1
    return nega_fibonacci(n + 2) - nega_fibonacci(n + 1)


k = 8
fib = [fibonacci(i) for i in range(1, k + 1)]
nega_fib = [nega_fibonacci(i) for i in range(-k, 1)]

print(nega_fib + fib)   # [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
