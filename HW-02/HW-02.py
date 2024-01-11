def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")


def check_win(board, player):
    # Проверка по горизонтали
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Проверка по вертикали
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    moves_left = 9

    while moves_left > 0:
        print_board(board)
        print(f"Ход игрока {players[current_player]}")
        row = int(input("Введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))

        if board[row][col] != " ":
            print("Эта ячейка уже занята. Попробуйте снова.")
            continue

        board[row][col] = players[current_player]
        moves_left -= 1

        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Игрок {players[current_player]} победил!")
            break

        current_player = (current_player + 1) % 2

    if moves_left == 0:
        print_board(board)
        print("Ничья!")


play_game()
