from enum import Enum
CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8
#Empty
_ = '_'

#White pawn and king
w = 'w'
W = 'W'

#Black pawn and king
b = 'b'
B = 'B'

#Players
PLAYERS = Enum("Players", "White Black")

def init_grid():
    #Initialize the new game grid
    grid = [[_, b, _, b, _, b, _, b],
            [b, _, b, _, b, _, b, _],
            [_, b, _, b, _, b, _, b],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [w, _, w, _, w, _, w, _],
            [_, w, _, w, _, w, _, w],
            [w, _, w, _, w, _, w, _]]
    return grid

def main():
    #Entry point
    print("Drafts")
    print("With this version of drafts the players must move diagonally\nand take pieces by jumping over them.")
    value_package = dict([("play_board", init_grid()), ("cur_turn", PLAYERS.Black)])
    board = init_grid()
    while True:
        print_board(board)
        move(value_package, board)

def print_board(board):
    #This function is drawing the board
    print("      1 2 3 4 5 6 7 8\n")
    for i in range(GRID_HEIGHT):
        print(i + 1, "   |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j] + "|", end="")
        print("")
    print("")

def coords(board, num):
    num = int(num) - 1
    return num % len(board), num // len(board)

def move(value_package, board):
    #this moves pieces
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn")
    #ask for move
        while True:
            src_x = int(input('Enter source x : '))
            src_y = int(input('Enter source y : '))
            dst_x = int(input('Enter destination x : '))
            dst_y = int(input('Enter destination y : '))

            src_x - 1
            src_y - 1

            dst_x - 1
            dst_y - 1
            
            mid_x = (src_x + dst_x) // 2
            mid_y = (src_y + dst_y) // 2

            if board[mid_y][mid_x] == '_':
                print('No piece to jump')
                break
                
            if board[src_y][src_x] == '_':
                print('empty cell')
                break

            if board[dst_y][dst_x] != '_':
                print('cell occupied')
                break

            if board[src_y][src_x] == board[mid_y][mid_x]:
                print('cant jump over piece with same colour')
                break

            #if board[dst_y][dst_x] != board[src_y][src_x] - 7 or board[src_y][src_x] - 9
                #print('invalid move')

            board[mid_y][mid_x] = '_'# or '_'
            board[src_y][src_x] = '_'# or '_'
            board[dst_y][dst_x] = 'w'

            value_package["cur_turn"] = PLAYERS.Black
            break
    else:
        print("Black's turn")
        while True:
            src_x = int(input('Enter source x : '))
            src_y = int(input('Enter source y : '))
            dst_x = int(input('Enter destination x : '))
            dst_y = int(input('Enter destination y : '))

            src_x - 1
            src_y - 1

            dst_x - 1
            dst_y - 1

            mid_x = (src_x + dst_x) // 2
            mid_y = (src_y + dst_y) // 2

            if board[mid_y][mid_x] == '_':
                print('No piece to jump')
                break

            if board[src_y][src_x] == '_':
                print('empty cell')
                break

            if board[dst_y][src_x] != '_':
                print('cell occupied')
                break

            if board[src_y][src_x] == board[mid_y][mid_x]:
                print('cant jump over piece with same colour')
                break

            board[mid_y][mid_x] = '_'
            board[src_y][src_x] = '_'
            board[dst_y][dst_x] = 'b'

            value_package["cur_turn"] = PLAYERS.White
            break

main()
