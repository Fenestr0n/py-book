# Найти повторяющиеся символы и заменить их на один такой символ.
text = input("Введите строку: ")    # I loove Pyythhon!!!!!
text += " "
newText = ""
i = 0
while i < len(text) - 1:
    if text[i] == text[i + 1]:
        i += 1
        continue
    else:
        newText += text[i]
    i += 1
print(newText)  # I love Python!