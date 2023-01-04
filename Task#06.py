# Написать программу, которая получает 3 целых числа.
# Выводит на экран сначала максимальное, затем минимальное и после оставшееся число.
numA = int(input("Введите первое число >>> "))
numB = int(input("Введите второе число >>> "))
numC = int(input("Введите третье число >>> "))

if numA < numB:
    numA, numB = numB, numA
if numA < numC:
    numA, numC = numC, numA
if numB > numC:
    numB, numC = numC, numB
print(numA, numB, numC)
