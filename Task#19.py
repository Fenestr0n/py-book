# Дана строка s = "aaabbbbcca". Преобразовать в "a3b4c2a1".
text = input("Введите строку > ")
text += " "   # Добавить пробел, чтобы не выйти за диапазон при проверке последнего элемента.
count = 1     # Счетчик повторяющихся символов.
i = 0
while i < len(text) - 1:
    if text[i] == text[i + 1]:
        count += 1
    else:
        print(text[i] + str(count), end="")
        count = 1
    i += 1
