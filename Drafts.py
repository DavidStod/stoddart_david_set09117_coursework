from enum import Enum
CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8
#Empty
E = '_'
_ = '#'
#White pawn and king
w = 'w'
W = 'W'

#Black pawn and king
b = 'b'
B = 'B'

#Players
PLAYERS = Enum("Players", "Black White")

def init_grid():
    #Initialize the new game grid
    grid = [[E, b, E, b, E, b, E, b],
            [b, E, b, E, b, E, b, E],
            [E, b, E, b, E, b, E, b],
            [_, E , _, E, _, E, _, E],
            [E, _, E, _, E, _, E, _],
            [w, E, w, E, w, E, w, E],
            [E, w, E, w, E, w, E, w],
            [w, E, w, E, w, E, w, E]]
    return grid

def main():
    #Entry point
    print("\nDrafts\n")
    print("With this version of drafts the players must move diagonally and take pieces by jumping over them.\nThe x coordinates are at the top and the y coordinates are on the left side.\n")
    value_package = dict([("play_board", init_grid()), ("cur_turn", PLAYERS.Black)])
    board = init_grid()
    while True:
        print_board(board)
        move(value_package, board)

def print_board(board):
    #This function is drawing the board
    print("\n      1 2 3 4 5 6 7 8 |X\n")
    for i in range(GRID_HEIGHT):
        print(i + 1, "   |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j] + "|", end="")
        print("")
    print("_\nY\n")

def coords(board, num):
    num = int(num) - 1
    return num % len(board), num // len(board)

def move(value_package, board):
    #this moves pieces
    if value_package["cur_turn"] == PLAYERS.White:

        ########### WHITE MOVEMENT ############

        print("\033[1;4;4;4;4m" + "White's Turn" + "\033[0m")
        while True:
#user input
            srcx = int(input('Enter piece X coordinate : '))
            srcy = int(input('Enter piece Y coordinate : '))
            dstx = int(input('Enter destination X coordinate : '))
            dsty = int(input('Enter destination Y coordinate: '))

            diffx = abs(srcx - dstx)
            diffy = abs(srcy - dsty)
#make values right for what the computer sees
            srcx = srcx - 1
            srcy = srcy - 1

            dstx = dstx - 1
            dsty = dsty - 1

            midx = abs(srcx + dstx) // 2
            midy = abs(srcy + dsty) // 2
#source is empty
            if board[srcy][srcx] == '#':
                print('empty cell')
                print_board(board)
                return move(value_package, board)
#choosing correct type of piece   
            if board[srcy][srcx] == 'b' or board[srcy][srcx] == 'B':
                print('Please choose your own piece')
                print_board(board)
                return move(value_package, board)
#in play area
            if board[srcy][srcx] == '_':
                print('choose starting value in play area')
                print_board(board)
                return move(value_package, board)

            if board[dsty][dstx] == '_':
                print('choose finishing value in play area')
                print_board(board)
                return move(value_package, board)

            if srcx < 0 or srcx > 7 or srcy < 0 or srcy > 7:
                print('Please choose valid source values')
                print_board(board)
                return move(value_package, board)
            if dstx < 0 or dstx > 7 or dsty < 0 or dsty > 7:
                print('Please choose valid destination values')
                print_board(board)
                return move(value_package, board)
#moves cant be to large
                if dstx > srcx + 2 or dstx < srcx - 2:
                    print('move too large')
                    print_board(board)
                    return move(value_package, board)

                if dsty > srcy + 2 or dsty < srcy - 2:
                    print('move too large')
                    print_board(board)
                    return move(value_package, board)
#moves cant be straight forward or sideways
                if dstx == srcx:
                    print('move diagonally')
                    print_board(board)
                    return move(value_package, board)
                if dsty == srcy:
                    print('move diagonally')
                    print_board(board)
                    return move(value_package, board)
#destination occupied
            if board[dsty][dstx] != '#':
                print('cell occupied')
                print_board(board)
                return move(value_package, board)
#taking a piece
            if board[midy][midx] == 'b' or board[midy][midx] == 'B':
                if board[srcy][srcx] == 'w':
                    board[srcy][srcx] = '#'
                    board[midy][midx] = '#'
                    board[dsty][dstx] = 'w'
                elif board[srcy][srcx] == 'W':
                    board[srcy][srcx] = '#'
                    board[midy][midx] = '#'
                    board[dsty][dstx] = 'W'
                print_board(board)
                answer = str(input("Any more pieces to take?(y/n)"))
                if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                    print_board(board)
                    return move(value_package, board)
                elif answer in ['n', 'N', 'no', 'No', 'NO']:
                    print_board(board)
                    value_package["cur_turn"] = PLAYERS.Black
                    return move(value_package, board)
#king movement different from pawn
            if board[srcy][srcx] == 'w' and srcy < dsty:
                print('cant move back')
                return move(value_package, board)
            elif board[srcy][srcx] == 'W' and srcy < dsty:
                midx = midx + 1
                midy = midy + 1

#jumping over same colour piece
            if board[srcy][srcx] == board[midy][midx]:
                print('cant jump over piece with same colour')
                return move(value_package, board)
#jumping blank piece
            if srcx == midx + 1:
                midx = midx + 1
                midy = midy + 1

            if board[midy][midx] == '#':
                print('No piece to jump')
                return move(value_package, board)
#general movement
            if board[srcy][srcx] == 'w':
                if dsty == 0:
                    print('Piece kinged')
                    board[srcy][srcx] = '#'
                    board[dsty][dstx] = 'W'
                else:
                    board[srcy][srcx] = '#'
                    board[dsty][dstx] = 'w'

            if board[srcy][srcx] == 'W':
                board[srcy][srcx] = '#'
                board[dsty][dstx] = 'W'
            
            value_package["cur_turn"] = PLAYERS.Black
            print_board(board)
            return move(value_package, board)
    else:

        ########### BLACK MOVEMENT ############

        print("\033[1;4m" + "Black's Turn" + "\033[0m")
        while True:
#user input
            srcx = int(input('Enter piece X coordinate : '))
            srcy = int(input('Enter piece Y coordinate : '))
            dstx = int(input('Enter destination X coordinate : '))
            dsty = int(input('Enter destination Y coordinate : '))

            diffx = abs(srcx - dstx)
            diffy = abs(srcy - dsty)
#make values right for what the computer sees            
            srcx = srcx - 1
            srcy = srcy - 1

            dstx = dstx - 1
            dsty = dsty - 1

            midx = abs(srcx + dstx) // 2
            midy = abs(srcy + dsty) // 2
#source is empty 
            if board[srcy][srcx] == '#':
                print('empty cell')
                print_board(board)
                return move(value_package, board)
#choosing correct type of piece           
            if board[srcy][srcx] == 'w' or board[srcy][srcx] == 'W':
                print('Please choose your own piece')
                print_board(board)
                return move(value_package, board)
#in play area
            if board[srcy][srcx] == '_':
                print('choose starting value in play area')
                print_board(board)
                return move(value_package, board)

            if board[dsty][dstx] == '_':
                print('choose finishing value in play area')
                print_board(board)
                return move(value_package, board)

            if srcx < 0 or srcx > 7 or srcy < 0 or srcy > 7:
                print('Please choose valid source values')
                print_board(board)
                return move(value_package, board)
            if dstx < 0 or dstx > 7 or dsty < 0 or dsty > 7:
                print('Please choose valid destination values')
                print_board(board)
                return move(value_package, board)
#moves cant be to large
            if dstx > srcx + 2 or dstx < srcx - 2:
                print('move too large')
                print_board(board)
                return move(value_package, board)

            if dsty > srcy + 2 or dsty < srcy - 2:
                print('move too large')
                print_board(board)
                return move(value_package, board)
#moves cant be straight forward or sideways
            if dstx == srcx:
                print('move diagonally')
                print_board(board)
                return move(value_package, board)
            if dsty == srcy:
                print('move diagonally')
                print_board(board)
                return move(value_package, board)
#destination occupied
            if board[dsty][dstx] != '#':
                print('cell occupied')
                print_board(board)
                return move(value_package, board)
#taking a piece
            if board[midy][midx] == 'w' or board[midy][midx] == 'W':
                if board[srcy][srcx] == 'b':
                    board[srcy][srcx] = '#'
                    board[midy][midx] = '#'
                    board[dsty][dstx] = 'b'

                elif board[srcy][srcx] == 'B':
                    board[srcy][srcx] = '#'
                    board[midy][midx] = '#'
                    board[dsty][dstx] = 'B'
                print_board(board)
                answer = str(input("Any more pieces to take?(y/n)"))
                if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                    print_board(board)
                    return move(value_package, board)
                elif answer in ['n', 'N', 'no', 'No', 'NO']:
                    print_board(board)
                    value_package["cur_turn"] = PLAYERS.White
                    return move(value_package, board)
#king movement different from pawn
            if board[srcy][srcx] == 'b' and srcy > dsty:
                print('cant move back')
                return move(value_package, board)
            elif board [srcy][srcx] == 'B' and srcy > dsty:
                midx = midx + 1
                midy = midy + 1
#jumping blank piece
            if board[midy][midx] == '#':
                print('No piece to jump')
                return move(value_package, board)
#jumping over same colour piece
            if srcx == midx:
                midx = midx + 1
                midy = midy + 1

            if board[srcy][srcx] == board[midy][midx]:
                print('cant jump over piece with same colour')
                return move(value_package, board)
#general movement
            if board[srcy][srcx] == 'b':
                if dsty == 7:
                    board[srcy][srcx] = '#'
                    board[dsty][dstx] = 'B'
                else:
                    board[srcy][srcx] = '#'
                    board[dsty][dstx] = 'b'
      
            if board[srcy][srcx] == 'B':
                board[srcy][srcx] = '#'
                board[dsty][dstx] = 'B'

            value_package["cur_turn"] = PLAYERS.White
            print_board(board)
            return move(value_package, board)

main()
