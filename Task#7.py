# Написать калькулятор + - / * mod pow div
# Деление на 0 -> ошибка
firstNumber = float(input("Первое число >>> "))
secondNumber = float(input("Второе число >>> "))
operation = input("Оператор [+ - / * mod pow div] >>> ")

if operation == "+":
    print(firstNumber + secondNumber)
elif operation == "-":
    print(firstNumber - secondNumber)
elif operation == "/":
    if secondNumber == 0:
        print("Ошибка! Деление на 0.")
    else:
        print(firstNumber / secondNumber)
elif operation == "*":
    print(firstNumber * secondNumber)
elif operation == "mod":
    if secondNumber == 0:
        print("Ошибка! Деление на 0")
    else:
        print(firstNumber % secondNumber)
elif operation == "pow":
    print(firstNumber ** secondNumber)
elif operation == "div":
    if secondNumber == 0:
        print("Ошибка! Деление на 0.")
    else:
        print(firstNumber // secondNumber)
else:
    print("Неизвестная команда")