# Является ли введенная строка палиндромом?
text = input("Введите строку >>> ")
reverseText = text[:: -1]
if reverseText == text:
    print("Палиндром")
else:
    print("Обычная строка")
