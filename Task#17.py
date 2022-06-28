# Найти все цифры и заменить их на букву латинского алфавита, располагающуюся по данному индексу.
text = input("Введите строку: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
number = ""
i = 0
while i < len(text):
    symbol = text[i]
    while symbol.isnumeric():
        number += symbol
        i += 1
        if i < len(text):
            symbol = text[i]
        else:
            break
    if number.isdigit():
        if 0 < int(number) <= len(alphabet):
            text = text.replace(number, alphabet[int(number) - 1], 1)
        else:
            text = text.replace(number, "*", 1)  # вне диапазона алфавита

        if len(number) > 1:
            i -= len(number) - 1  # n знаков числа заменили 1 буквой, откат индекса.
        number = ""
    i += 1
print(text)
# Hel12o 16e15ple -> Hello people
# H555l12o 16e15pl0 -> H*llo peopl*