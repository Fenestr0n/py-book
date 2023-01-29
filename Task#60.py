# Создайте программу для игры в "Крестики-нолики"

# Инициализация
board = list(range(1, 10))
win_lines= [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]


# Отрисовка игровой доски
def draw_board(board):
    for i in range(3):
        print(board[0 + i * 3], board[1 + i * 3], board[2 + i * 3])


# Проверка игрового поля
def check_win(board):
    for line in win_lines:
        if board[line[0]] == "X" and board[line[1]] == "X" and board[line[2]] == "X":
            return "X"    # Вернуть выигрышный символ
        elif board[line[0]] == "O" and board[line[1]] == "O" and board[line[2]] == "O":
            return "O"


# Сделать ход
def step_game(symbol):
    while True:
        try:
            pos = int(input(f"Введите позицию '{symbol}': "))
        except ValueError:
            continue
        if pos >= 1 and pos <= 9:
            if str(board[pos - 1]).isdigit():
                board[pos - 1] = symbol     # Изменить имеющийся список board
                break


# tic-tac-toe
def game(board):
    count = 0
    while True:
        draw_board(board)
        if count % 2 == 0:
            step_game('X')
        else:
            step_game('O')
        count += 1
        smb = check_win(board)
        if smb:
            print(f"Выиграл '{smb}'!")
            break
        if count == 9:
            print("Ничья!")
            break

game(board)