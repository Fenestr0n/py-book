# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
'''
5, 25 -> да
4, 16 -> да
25, 5 -> да
8, 9 -> нет
'''

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 == num2**2 or num2 == num1**2:
    print("Да")
else:
    print("Нет")
