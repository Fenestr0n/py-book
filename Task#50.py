# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
'''
Пример:
45 -> 101101
3 -> 11
2 -> 10
'''
# print(bin(45)) #"0b101101"
# print(bin(3))  #"0b11"
# print(bin(2))  #"0b10"


def num_to_binary(num):
    s = ''
    while num > 0:
        s = str(num % 2) + s
        num = num // 2
    return int(s)


assert num_to_binary(45) == 101101
assert num_to_binary(3) == 11
assert num_to_binary(2) == 10
