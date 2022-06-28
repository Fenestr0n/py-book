# Реализовать класс, который будет разделять целую и дробную часть числа с плавающей точкой.
# Вывести на экран результат суммы или произведения введенного пользователем числа с любой из этих частей.
from decimal import Decimal

class Fraction:
    def __init__(self, number):
        self.__first = int(number)
        num = Decimal(str(number - self.__first))
        self.__second = num.quantize(Decimal("1.000"))

    def Sum(self, a, part):
        if part == "1":
            return a + self.__first
        elif part == "2":
            return a + self.__second
        else:
            print("Неверный ввод")

    def Multiply(self, a, part):
        if part == "1":
            return a * self.__first
        elif part == "2":
            return a * self.__second
        else:
            print("Неверный ввод")

n = float(input("> "))
fract = Fraction(n)

while True:
    num_ = int(input("Число >"))
    part = input("Часть числа >")
    if part == "end":
        break
    print(fract.Sum(num_, part))
    print(fract.Multiply(num_, part))