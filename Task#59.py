# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from random import randint 


def create_data():
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    with open("input_data.txt", "w") as file:
        for i in range(1, 21):
            pos = randint(0, len(alphabet) - 1)
            number = randint(1, 5)
            file.write(alphabet[pos] * number)


def encode_txt(text):
    text += " "
    count = 1     
    i = 0
    result = ""
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            count += 1
        else:
            result += str(count) + text[i]
            count = 1
        i += 1
    return result


def decode_rle(text):
    i = 0
    result = ""
    while i < len(text):
        if text[i].isdigit():
            result += int(text[i]) * text[i + 1]
        i += 1
    return result


create_data()

with open("input_data.txt", "r", encoding="utf8") as file:
    txt = file.readline()

with open("output_data.txt", "w") as file:
    rle = encode_txt(txt)
    dec = decode_rle(rle)
    
    file.write(rle + "\n")
    file.write(dec)