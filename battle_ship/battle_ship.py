import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, points):
        self.points = points


class Board:
    def __init__(self, ships):
        self.ships = ships
        self.size = 6
        self.board = [['О' for _ in range(self.size)] for _ in range(self.size)]

    def place_ships(self):
        for ship in self.ships:
            for point in ship.points:
                self.board[point.x][point.y] = '■'

    def display_board(self):
        print("   | 1 | 2 | 3 | 4 | 5 | 6 |")
        print("-----------------------------")
        for i, row in enumerate(self.board):
            print(f" {i + 1} | {' | '.join(row)} |")
            print("-----------------------------")

    def player_turn(self):
        x = int(input("Введите номер строки (от 1 до 6): ")) - 1
        y = int(input("Введите номер столбца (от 1 до 6): ")) - 1

        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise Exception("Вы стрельнули за пределы вселенной! Цельтесь точнее!")

        if self.board[x][y] == 'X' or self.board[x][y] == 'T':
            raise Exception("Вы уже стреляли в эту клетку!")

        if self.board[x][y] == '■':
            self.board[x][y] = 'X'
            print("Вы попали!")
        else:
            self.board[x][y] = 'T'
            print("Вы промахнулись!")

        self.display_board()

    def computer_turn(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        if self.board[x][y] == 'X' or self.board[x][y] == 'T':
            self.computer_turn()

        if self.board[x][y] == '■':
            self.board[x][y] = 'X'
            print("Компьютер попал!")
        else:
            self.board[x][y] = 'T'
            print("Компьютер промахнулся!")

        self.display_board()

    def check_game_over(self):
        for row in self.board:
            if '■' in row:
                return False
        return True


# Создание кораблей
ship1 = Ship([Point(0, 0), Point(0, 1), Point(0, 2)])
ship2 = Ship([Point(1, 3), Point(1, 4)])
ship3 = Ship([Point(4, 0), Point(4, 2), Point(4, 4), Point(4, 5)])
ship4 = Ship([Point(5, 0)])

# Создание досок
player_board = Board([ship1, ship2, ship3, ship4])
computer_board = Board([ship1, ship2, ship3, ship4])

# Размещение кораблей на досках
player_board.place_ships()
computer_board.place_ships()

# Игровой цикл
while True:
    try:
        player_board.player_turn()
        if player_board.check_game_over():
            print("Вы победили!")
            break

        computer_board.computer_turn()
        if computer_board.check_game_over():
            print("Компьютер победил!")
            break
    except Exception as e:
        print(e)