# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
while True:
    get_day = input("Введите номер дня недели: ")
    if get_day.isdigit():
        if int(get_day) in range(1, 6):
            print("Рабочий день")
            break
        elif int(get_day) in range(6, 8):
            print("Выходной")
            break
