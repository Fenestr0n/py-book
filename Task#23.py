"""Дана строка в виде случайной последовательности чисел от 0 до 9.
Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
а в качестве значений – количество этих чисел в имеющейся последовательности.
Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
"""


def count_it(sequence):
    dictionary = {i: sequence.count(i) for i in sequence}
    result = {}
    for _ in range(1, 4):
        maxValue = max(dictionary.values())
        current = {key: value for key, value in dictionary.items() if value == maxValue}
        result.update(current)
        for key in current.keys():
           del dictionary[key]
    return result


str = input("> ")       # 2122234555768290909389
print(count_it(str))    # {'2': 5, '9': 4, '5': 3}