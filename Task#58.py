# Создайте программу для игры с конфетами человек против человека.
'''Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
'''

from random import randint

print("Жеребьёвка...")
player = randint(0, 2)
num_candy = 2021
count_1 = 0
count_2 = 0


def take_candy():
    while True:
        get_candy = input("Введите количество конфет: ")
        if get_candy.isdigit():
            if int(get_candy) in range(1, 29):
                break
    return int(get_candy)


while num_candy > 28:
    if player == 0:
        print("Ход первого игрока")
        item = take_candy()
        count_1 += item
        num_candy -= item
        player = 1
        print(f"Всего: {num_candy}\tПервый игрок: {count_1}\tВторой игрок: {count_2}")
    else:
        print("Ход второго игрока")
        item = take_candy()
        count_2 += item
        num_candy -= item
        player = 0
        print(f"Всего: {num_candy}\tПервый игрок: {count_1}\tВторой игрок: {count_2}")
else:
    
    if player == 0:
        count_1 += num_candy
        print(f"Оставшиеся {num_candy} конфет достаются первому игроку")
        print(f"Выиграл первый игрок со счетом {count_1} : {count_2}")
    else:
        count_2 += num_candy
        print(f"Оставшиеся {num_candy} конфет достаются второму игроку")
        print(f"Выиграл второй игрок со счетом {count_2} : {count_1}")

print(f"Первому игроку нужно взять {2021 % 29} конфет, чтобы забрать все конфенты у конкурента.")