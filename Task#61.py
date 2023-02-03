# tic-tac-toe

# list comprehension and zip()
board = [i for i in range(1, 10)]

x = [0, 3, 6, 0, 1, 2, 0, 2]
y = [1, 4, 7, 3, 4, 5, 4, 4]
z = [2, 5, 8, 6, 7, 8, 8, 6]
win_lines = list(zip(x, y, z))


def draw_board(board):
    _ = [print(board[0 + i * 3], board[1 + i * 3], board[2 + i * 3]) for i in range(3)]


def check_win(board):
    for line in win_lines:
        if board[line[0]] == "X" and board[line[1]] == "X" and board[line[2]] == "X":
            return "X"
        elif board[line[0]] == "O" and board[line[1]] == "O" and board[line[2]] == "O":
            return "O"


def step_game(symbol):
    while True:
        try:
            pos = int(input(f"Введите позицию '{symbol}': "))
        except ValueError:
            continue
        if pos >= 1 and pos <= 9:
            if str(board[pos - 1]).isdigit():
                board[pos - 1] = symbol
                break


count = 0
while True:
    draw_board(board)
    if not count % 2:
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