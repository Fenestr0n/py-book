# Напишите программу, которая принимает на вход 5 чисел и находит максимальное из них.

max = 0


for i in range(5):
    num = int(input(f"Введите число {i+1}: "))
    if num > max:
        max = num

print(max)