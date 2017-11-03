from enum import Enum
CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8
#Empty
E = '_'

#White pawn and king
Wp = 'w'
Wk = 'W'

#Black pawn and king
Bp = 'b'
Bk = 'B'

#Players
PLAYERS = Enum("Players", "White Black")

def main():
    #Entry point
    print("Drafts")
    print("With this version of drafts the players must move diagonally\nand take pieces by jumping over them.")
    value_package = dict([("play_board", init_grid()), ("turn_count", 1), ("cur_turn", PLAYERS.Black)])
    board = init_grid()
    while True:
        move(value_package, board)

def init_grid():
    #Initialize the new game grid
    grid = [[E, Bp, E, Bp, E, Bp, E, Bp],
            [Bp, E, Bp, E, Bp, E, Bp, E],
            [E, Bp, E, Bp, E, Bp, E, Bp],
            [E, E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E, E], 
            [Wp, E, Wp, E, Wp, E, Wp, E],
            [E, Wp, E, Wp, E, Wp, E, Wp],
            [Wp, E, Wp, E, Wp, E, Wp, E]]
    return grid

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
    print("Turn : ", value_package["turn_count"])
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn :\n")
        print_board(value_package["play_board"])
    #ask for move
        while True:
            m = input('Enter move : ')
            try:
                return int(float(m))
            except:
                print("({0}) isnt a numeric value".format(m))
                return move(value_package, board)
            (src_x, src_y), (dst_x, dst_y) = (coords(board, x) for x in jump.split())
            
            mid_x = (src_x + dst_x) // 2
            mid_y = (src_y + dst_y) // 2

            if board[mid_y][mid_x] == 'E':# or '_'
                print('No piece to jump')
                
            if board[src_y][src_x] == 'E':# or '_'
                print('empty cell')

            if board[dst_y][dst_x] != 'E':# or '_'
                print('cell occupied')

            if board[src_y][src_x] == board[mid_y][mid_x]:
                print('cant jump over piece with same colour')

            #if board[dst_y][dst_x] != board[src_y][src_x] - 7 or board[src_y][src_x] - 9
                #print('invalid move')

            board[dst_y][dst_x] = board[src_y][src_x]
            board[mid_y][mid_x] = 'E'# or '_'
            board[src_y][src_x] = 'E'# or '_'

            value_package["cur_turn"] = PLAYERS.Black
            value_package["turn_count"] + 1
            move(board, jump)
            print_board(board)
            break
    else:
        print("Black's turn :\n")
        print_board(value_package["play_board"])
        while True:
            m = input("Enter move : ")
            try:
                return int(float(m))
            except:
                print("({0}) isnt a numeric value".format(m))
                return move(value_package, board)
            (src_x, src_y), (dst_x, dst_y) = (coords(board, x) for x in jump.split())
            
            mid_x = (src_x + dst_x) // 2
            mid_y = (src_y + dst_y) // 2

            if board[mid_y][mid_x] == '_':# or 'E'
                print('No piece to jump')

            if board[src_y][src_x] == '_':# or 'E'
                print('empty cell')

            if board[dst_y][src_x] !='_':# or 'E'
                print('cell occupied')

            if board[src_y][src_x] == board[mid_y][mid_x]:
                print('cant jump over piece with same colour')

            board[dst_y][dst_x] = board[src_y][src_x]
            board[mid_y][mid_x] = '_'# or 'E'
            board[src_y][src_x] = '_'# or 'E'
            value_package["cur_turn"] = PLAYERS.White
            value_package["turn_count"] + 1
            move(board, jump)
            print_board(board)
            break

main()
