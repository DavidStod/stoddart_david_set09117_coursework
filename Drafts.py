from enum import Enum
from random import randint
CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8
#Empty
_ = '_'
E = '#'
#White pawn and king
r = '\033[31m' + 'r' + '\033[0m'
R = '\033[31m' + 'R' + '\033[0m'

#Black pawn and king
b = 'b'
B = 'B'

#Players
PLAYERS = Enum("Players", "Black Red")

#amout of pieces each side has
black_pieces = 12
red_pieces = 12

#try count if player cant move
try_count = 1

#count the turns
turn_count = 1

#undo variables
usrcx = 0
usrcy = 0
udstx = 0
udsty = 0

def init_grid():
    #Initialize the new game grid
    grid = [[_, b, _, b, _, b, _, b],
            [b, _, b, _, b, _, b, _],
            [_, b, _, b, _, b, _, b],
            [E, _, E, _, E, _, E, _],
            [_, E, _, E, _, E, _, E],
            [r, _, r, _, r, _, r, _],
            [_, r, _, r, _, r, _, r],
            [r, _, r, _, r, _, r, _]]
    return grid

def main():
    #Entry point
    print("\nDrafts\n")
    print("With this version of drafts the players must move diagonally and take pieces by jumping over them.\nThe x coordinates are at the top and the y coordinates are on the left side.\nPlayers have three attempts to take their move or the game will be a draw.\n")
    value_package = dict([("play_board", init_grid()), ("cur_turn", PLAYERS.Black)])
    board = init_grid()
    game = input('2 player or 1 player plus ai? ')
    if game == '2':
        print_board(board)
        move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
    elif game == '1':
        print_board(board)
        ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

def print_board(board):
    #This function is drawing the board
    print("\n      1 2 3 4 5 6 7 8 |X\n")
    for i in range(GRID_HEIGHT):
        print(i + 1, "   |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j] + "|", end="")
        print("")
    print("_\nY\n")

def move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty):
#checks how many attempts players have left 
    if try_count == 4:
        print('Turn can not be taken. Its a draw')
        exit()
    print("\033[1;4m" + "Try :", try_count)
    #this moves pieces
    if value_package["cur_turn"] == PLAYERS.Red:

        ########### RED MOVEMENT ############
        print("Red's Turn" + "\033[0m")
        choice = input('Press any key to move or type exit to exit or undo to undo: ')
        if choice == 'exit':
            exit()
        elif choice == 'undo':
            umidx = abs(usrcx + udstx) // 2
            umidy = abs(usrcy + udsty) // 2
            if board[usrcy][usrcx] == B:
                if usrcy == 0 and board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = r
                    board[udsty][udstx] = b
                    black_pieces = black_pieces + 1
                elif usrcy != 0 and board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = r
                    board[udsty][udstx] = B
                    black_pieces = black_pieces + 1
                elif usrcy == 0:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = b
                elif usrcy != 0:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = B
            if board[usrcy][usrcx] == b:
                if board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = r
                    board[udsty][udstx] = b
                elif board[umidy][umidx] != E:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = b
            value_package["cur_turn"] = PLAYERS.Black
            print_board(board)
            return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
        while True:
#user input
            #srcx input
            while True:
                try:
                    srcx = int(input('Enter piece X coordinate : '))
                    break
                except:
                    print("Please enter a number value between 1 and 8")
            
            #srcy input
            while True:
                try:
                    srcy = int(input('Enter piece Y coordinate : '))
                    break
                except:
                    print("Please enter a number value between 1 and 8")
            #dstx input
            while True:
                try:
                    dstx = int(input('Enter destination X coordinate : '))
                    break    
                except:
                    print("Please enter a number value between 1 and 8")
            #dsty input
            while True:
                try:
                    dsty = int(input('Enter destination Y coordinate: '))
                    break
                except:
                    print("Please enter a number value between 1 and 8")
            
            if srcx < 0 or srcx > 7:
                print("Input X coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if srcy < 0 or srcy > 7:
                print("Input Y coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if dstx < 0 or dstx > 7:
                print("Input X coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if dsty < 0 or dsty > 7:
                print("Input Y coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

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
            if board[srcy][srcx] == E:
                print('empty cell')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#choosing correct type of piece   
            if board[srcy][srcx] == b or board[srcy][srcx] == B:
                print('Please choose your own piece')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#in play area
            if board[srcy][srcx] == _:
                print('choose starting value in play area')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if board[dsty][dstx] == _:
                print('choose finishing value in play area')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#moves cant be to large
                if dstx > srcx + 2 or dstx < srcx - 2:
                    print('move too large')
                    print_board(board)
                    return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

                if dsty > srcy + 2 or dsty < srcy - 2:
                    print('move too large')
                    print_board(board)
                    return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#moves cant be straight forward or sideways
                if dstx == srcx:
                    print('move diagonally')
                    print_board(board)
                    return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
                if dsty == srcy:
                    print('move diagonally')
                    print_board(board)
                    return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#destination occupied
            if board[dsty][dstx] != E:
                print('cell occupied')
                print_board(board)
                try_count = try_count + 1
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#pawn movement
            if board[srcy][srcx] == r and srcy < dsty:
                print('cant move back')
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#taking a piece
            if board[midy][midx] == b or board[midy][midx] == B:
                if board[srcy][srcx] == r:
                    if dsty == 0:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = R
                        red_pieces = red_pieces - 1
                        usrcx = dstx
                        usrcy = dsty
                        udstx = srcx
                        udsty = srcy
                    else:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = r
                        red_pieces = red_pieces - 1
                        usrcx = dstx
                        usrcy = dsty
                        udstx = srcx
                        udsty = srcy
                elif board[srcy][srcx] == R:
                    board[srcy][srcx] = E
                    board[midy][midx] = E
                    board[dsty][dstx] = R
                    red_pieces = red_pieces - 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy
                print_board(board)
                try_count = 1
                #if no pieces left this shows 
                if red_pieces == 0:
                    print('Red won')
                    exit()
                #if more pieces to take
                while True:
                    answer = str(input("Any more pieces to take?(y/n)"))
                    if answer not in ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no' 'No', 'NO'):
                        print("Not acceptable answer please try again")
                        continue
                    if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                        print_board(board)
                        return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
                    elif answer in ['n', 'N', 'no', 'No', 'NO']:
                        print_board(board)
                        value_package["cur_turn"] = PLAYERS.Black
                        return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#king movement different from pawn
            if board[srcy][srcx] == R and srcy < dsty:
                midx = midx + 1
                midy = midy + 1
                try_count = 1

#jumping over same colour piece
            if board[srcy][srcx] == board[midy][midx]:
                print('cant jump over piece with same colour')
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#jumping blank piece
            if srcx == midx + 1:
                midx = midx + 1
                midy = midy + 1

            if board[midy][midx] == E:
                print('No piece to jump')
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#general movement
            if board[srcy][srcx] == r:
                if dsty == 0:
                    print('Piece kinged')
                    board[srcy][srcx] = E
                    board[dsty][dstx] = R
                    try_count = 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy
                else:
                    board[srcy][srcx] = E
                    board[dsty][dstx] = r
                    try_count = 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy

            if board[srcy][srcx] == R:
                board[srcy][srcx] = E
                board[dsty][dstx] = R
                try_count = 1
                usrcx = dstx
                usrcy = dsty
                udstx = srcx
                udsty = srcy
            
            value_package["cur_turn"] = PLAYERS.Black
            print_board(board)
            return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
    else:

        ########### BLACK MOVEMENT ############

        print("Black's Turn" + "\033[0m")
        choice = input('Press any key to move or type exit to exit or undo to undo: ')
        #exit at anytime
        if choice == 'exit':
            exit()
        #undo function
        elif choice == 'undo':
            umidx = abs(usrcx + udstx) // 2
            umidy = abs(usrcy + udsty) // 2
            if board[usrcy][usrcx] == R:
                if usrcy == 0 and board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = b
                    board[udsty][udstx] = r
                    red_pieces = red_pieces + 1
                elif usrcy != 0 and board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = b
                    board[udsty][udstx] = R
                    red_pieces = red_pieces + 1
                elif usrcy == 0:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = r
                elif usrcy != 0:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = R
            if board[usrcy][usrcx] == r:
                if board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = b
                    board[udsty][udstx] = r
                    red_pieces = red_pieces + 1
                elif board[umidy][umidx] != E:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = r
            value_package["cur_turn"] = PLAYERS.Red
            print_board(board)
            return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
        while True:
#user input
            #srcx input
            while True:
                try:
                    srcx = int(input('Enter piece X coordinate : '))
                    break
                except:
                    print('Please enter a number value between 1 and 8')
            #srcy input
            while True:
                try:
                    srcy = int(input('Enter piece Y coordinate : '))
                    break
                except:
                    print("Please enter a number value between 1 and 8")
            #dstx input
            while True:
                try:
                    dstx = int(input('Enter destination X coordinate : '))
                    break
                except:
                    print("Please enter a number value between 1 and 8")
            #dsty input
            while True:
                try:
                    dsty = int(input('Enter destination Y coordinate : '))
                    break
                except:
                    print("Please enter a number value between 1 and 8")
            
            if srcx < 0 or srcx > 7:
                print("Input X coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if srcy < 0 or srcy > 7:
                print("Input Y coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if dstx < 0 or dstx > 7:
                print("Input X coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if dsty < 0 or dsty > 7:
                print("Input Y coordinate between 1 and 8")
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

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
            if board[srcy][srcx] == E:
                print('empty cell')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#choosing correct type of piece           
            if board[srcy][srcx] == r or board[srcy][srcx] == R:
                print('Please choose your own piece')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#in play area
            if board[srcy][srcx] == _:
                print('choose starting value in play area')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if board[dsty][dstx] == _:
                print('choose finishing value in play area')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#moves cant be to large
            if dstx > srcx + 2 or dstx < srcx - 2:
                print('move too large')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if dsty > srcy + 2 or dsty < srcy - 2:
                print('move too large')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#moves cant be straight forward or sideways
            if dstx == srcx:
                print('move diagonally')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            if dsty == srcy:
                print('move diagonally')
                print_board(board)
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#destination occupied
            if board[dsty][dstx] != E:
                print('cell occupied')
                print_board(board)
                try_count = try_count + 1
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#pawn movement
            if board[srcy][srcx] == b and srcy > dsty:
                print('cant move back')
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#taking a piece
            if board[midy][midx] == r or board[midy][midx] == R:
                if board[srcy][srcx] == b:
                    if dsty == 7:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = B
                        black_pieces = black_pieces - 1
                        usrcx = dstx
                        usrcy = dsty
                        udstx = srcx
                        udsty = srcy
                    else:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = b
                        black_pieces = black_pieces - 1
                        usrcx = dstx
                        usrcy = dsty
                        udstx = srcx
                        udsty = srcy
                elif board[srcy][srcx] == B:
                    board[srcy][srcx] = E
                    board[midy][midx] = E
                    board[dsty][dstx] = B
                    black_pieces = black_pieces - 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy
                print_board(board)
                try_count = 1
                #if no more pieces shows this
                if black_pieces == 0:
                    print('Black won')
                    exit()
                #if more pieces to take
                while True:
                    answer = str(input("Any more pieces to take?(y/n)"))
                    if answer not in ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no' 'No', 'NO'):
                        print("Not acceptable answer please try again")
                        continue
                    
                    if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                        print_board(board)
                        return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
                    elif answer in ['n', 'N', 'no', 'No', 'NO']:
                        print_board(board)
                        value_package["cur_turn"] = PLAYERS.Red
                        return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#king movement different from pawn
            if board [srcy][srcx] == B and srcy > dsty:
                midx = midx + 1
                midy = midy + 1
#jumping blank piece
            if board[midy][midx] == E:
                print('No piece to jump')
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#jumping over same colour piece
            if srcx == midx:
                midx = midx + 1
                midy = midy + 1
            if board[srcy][srcx] == board[midy][midx]:
                print('cant jump over piece with same colour')
                return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#general movement
            if board[srcy][srcx] == b:
                if dsty == 7:
                    board[srcy][srcx] = E
                    board[dsty][dstx] = B
                    try_count = 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy
                else:
                    board[srcy][srcx] = E
                    board[dsty][dstx] = b
                    try_count = 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy
      
            if board[srcy][srcx] == B:
                board[srcy][srcx] = E
                board[dsty][dstx] = B
                try_count = 1
                usrcx = dstx
                usrcy = dsty
                udstx = srcx
                udsty = srcy

            value_package["cur_turn"] = PLAYERS.Red
            print_board(board)
            return move(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)


##################################
############ AI STUFF ############
##################################

def ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty):
    #checks how many attempts players have left 
    if try_count == 4:
        print('Turn can not be taken. Its a draw')
        exit()
    #this moves pieces
    if value_package["cur_turn"] == PLAYERS.Red:

        ########### RED MOVEMENT ############
        print("\033[1;4m" + "Try :", try_count)
        print("Red's Turn" + "\033[0m")
        choice = input('Press any key to move or type exit to exit or undo to undo : ')
        if choice == 'exit':
            exit()
        elif choice == 'undo':
            umidx = abs(usrcx + udstx) // 2
            umidy = abs(usrcy + udsty) // 2
            if board[usrcy][usrcx] == B:
                if usrcy == 0 and board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = r
                    board[udsty][udstx] = b
                    black_pieces = black_pieces + 1
                elif usrcy != 0 and board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = r
                    board[udsty][udstx] = B
                    black_pieces = black_pieces + 1
                elif usrcy == 0:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = b
                elif usrcy != 0:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = B
            if board[usrcy][usrcx] == b:
                if board[umidy][umidx] == E:
                    board[usrcy][usrcx] = E
                    board[umidy][umidx] = r
                    board[udsty][udstx] = b
                elif board[umidy][umidx] != E:
                    board[usrcy][usrcx] = E
                    board[udsty][udstx] = b
            value_package["cur_turn"] = PLAYERS.Black
            print_board(board)
            return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
        while True:
#user input
            #srcx input
            try:
                srcx = int(input('Enter piece X coordinate : '))
                if not 0<srcx<9:
                    print("Not in range input between 1 and 8")
                    return srcx
            except:
                print("Please enter a number value between 1 and 8")
                return srcx
            #srcy input
            try:
                srcy = int(input('Enter piece Y coordinate : '))
                if not 0<srcy<9:
                    print("Not in range input between 1 and 8")
                    return srcy
            except:
                print("Please enter a number value between 1 and 8")
                return srcy
            #dstx input
            try:
                dstx = int(input('Enter destination X coordinate : '))
                if not 0<dstx<9:
                    print("Not in range input between 1 and 8")
                    return dstx
            except:
                print("Please enter a number value between 1 and 8")
                return dstx
            #dsty input
            try:
                dsty = int(input('Enter destination Y coordinate: '))
                if not 0<dsty<9:
                    print("Not in range input between 1 and 8")
                    return dsty
            except:
                print("Please enter a number value between 1 and 8")
                return dsty

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
            if board[srcy][srcx] == E:
                print('empty cell')
                print_board(board)
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#choosing correct type of piece   
            if board[srcy][srcx] == b or board[srcy][srcx] == B:
                print('Please choose your own piece')
                print_board(board)
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#in play area
            if board[srcy][srcx] == _:
                print('choose starting value in play area')
                print_board(board)
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

            if board[dsty][dstx] == _:
                print('choose finishing value in play area')
                print_board(board)
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#moves cant be to large
                if dstx > srcx + 2 or dstx < srcx - 2:
                    print('move too large')
                    print_board(board)
                    return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)

                if dsty > srcy + 2 or dsty < srcy - 2:
                    print('move too large')
                    print_board(board)
                    return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#moves cant be straight forward or sideways
                if dstx == srcx:
                    print('move diagonally')
                    print_board(board)
                    return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
                if dsty == srcy:
                    print('move diagonally')
                    print_board(board)
                    return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#destination occupied
            if board[dsty][dstx] != E:
                print('cell occupied')
                print_board(board)
                try_count = try_count + 1
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#pawn movement
            if board[srcy][srcx] == r and srcy < dsty:
                print('cant move back')
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#taking a piece
            if board[midy][midx] == b or board[midy][midx] == B:
                if board[srcy][srcx] == r:
                    if dsty == 0:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = R
                        red_pieces = red_pieces - 1
                        usrcx = dstx
                        usrcy = dsty
                        udstx = srcx
                        udsty = srcy
                    else:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = r
                        red_pieces = red_pieces - 1
                        usrcx = dstx
                        usrcy = dsty
                        udstx = srcx
                        udsty = srcy
                elif board[srcy][srcx] == R:
                    board[srcy][srcx] = E
                    board[midy][midx] = E
                    board[dsty][dstx] = R
                    red_pieces = red_pieces - 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy
                print_board(board)
                try_count = 1
                #if no pieces left this shows 
                if red_pieces == 0:
                    print('Red won')
                    exit()
                #if more pieces to take
                while True:
                    answer = str(input("Any more pieces to take?(y/n)"))
                    if answer not in ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no' 'No', 'NO'):
                        print("Not acceptable answer please try again")
                        continue
                    if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                        print_board(board)
                        return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
                    elif answer in ['n', 'N', 'no', 'No', 'NO']:
                        print_board(board)
                        value_package["cur_turn"] = PLAYERS.Black
                        return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#king movement different from pawn
            if board[srcy][srcx] == R and srcy < dsty:
                midx = midx + 1
                midy = midy + 1
                try_count = 1

#jumping over same colour piece
            if board[srcy][srcx] == board[midy][midx]:
                print('cant jump over piece with same colour')
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#jumping blank piece
            if srcx == midx + 1:
                midx = midx + 1
                midy = midy + 1

            if board[midy][midx] == E:
                print('No piece to jump')
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
#general movement
            if board[srcy][srcx] == r:
                if dsty == 0:
                    print('Piece kinged')
                    board[srcy][srcx] = E
                    board[dsty][dstx] = R
                    try_count = 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy
                else:
                    board[srcy][srcx] = E
                    board[dsty][dstx] = r
                    try_count = 1
                    usrcx = dstx
                    usrcy = dsty
                    udstx = srcx
                    udsty = srcy

            if board[srcy][srcx] == R:
                board[srcy][srcx] = E
                board[dsty][dstx] = R
                try_count = 1
                usrcx = dstx
                usrcy = dsty
                udstx = srcx
                udsty = srcy
            
            value_package["cur_turn"] = PLAYERS.Black
            print_board(board)
            print("\033[1:4m" + "Black Turn" + "\033[0m")
            return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
    else:
        while True:
            srcx = randint(0,7)
            srcy = randint(0,7)
            dstx = randint(0,7)
            dsty = randint(0,7)
            #source is empty
            if board[srcy][srcx] == E:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #choosing correct type of piece
            if board[srcy][srcx] == r or board[srcy][srcx] == R:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #in play area
            if board[srcy][srcx] == _:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            if board[dsty][dstx] == _:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #moves cant be to large
            if dstx > srcx + 2 or dstx < srcx - 2:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            if dsty > srcy + 2 or dsty < srcy - 2:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #moves cant be straight forward or sideways
            if dstx == srcx:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            if dsty == srcy:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #destination occupied
            if board[dsty][dstx] != E:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            
            midx = abs(srcx + dstx) // 2
            midy = abs(srcy + dsty) // 2
            #pawn movement
            if board[srcy][srcx] == b and srcy > dsty:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #taking a piece
            if board[midy][midx] == r or board[midy][midx] == R:
                if board[srcy][srcx] == b:
                    if dsty == 7:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = B
                        black_pieces = black_pieces - 1
                    else:
                        board[srcy][srcx] = E
                        board[midy][midx] = E
                        board[dsty][dstx] = b
                        black_pieces = black_pieces - 1
                elif board[srcy][srcx] == B:
                    board[srcy][srcx] = E
                    board[midy][midx] = E
                    board[dsty][dstx] = B
                    black_pieces = black_pieces - 1
                if black_pieces == 0:
                    print('Black won')
                    exit()
            #king movement different from pawn
            if board [srcy][srcx] == B and srcy > dsty:
                midx = midx + 1
                midy = midy + 1
            #jumping blank piece
            if board[midy][midx] == E:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #jumping over same colour piece
            if srcx == midx:
                midx = midx + 1
                midy = midy + 1
            if board[srcy][srcx] == board[midy][midx]:
                return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)
            #general movement
            if board[srcy][srcx] == b:
                if dsty == 7:
                    board[srcy][srcx] = E
                    board[dsty][dstx] = B
                else:
                    board[srcy][srcx] = E
                    board[dsty][dstx] = b
            if board[srcy][srcx] == B:
                board[srcy][srcx] = E
                board[dsty][dstx] = B

            value_package["cur_turn"] = PLAYERS.Red
            print_board(board)
            return ai(value_package, board, red_pieces, black_pieces, try_count, turn_count, usrcx, usrcy, udstx, udsty)


main()
