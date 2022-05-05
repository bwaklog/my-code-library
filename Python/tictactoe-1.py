board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}


def printBoard(board):
    print(f'''
    {board[1]} | {board[2]} | {board[3]}
    ----------
    {board[4]} | {board[5]} | {board[6]}
    ----------
    {board[7]} | {board[8]} | {board[9]}
    ''')


printBoard(board=board)


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False

    return True


def checkForWin():
    # Rows
    if (board[1] == board[2] and board[1] == board[3] and board[1] != 1):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != 1):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != 1):
        return True

    # Column
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != 1):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != 1):
        return True
    elif (board[3] == board[6] and board[3] == board[8] and board[3] != 1):
        return True

    # Principal Diagonal
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != 1):
        return True

    # Off Diagonal
    elif (board[3] == board[5] and board[3] == board[7] and board[3] != 1):
        return True

    else:
        return False


def spaceIsFree(position):
    if(board[position] == ' '):  # if space is empty !
        return True
    else:
        return False


def insertLetter(letter, position):

    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if(checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'x':
                print("Bot wins")
                exit()
            else:
                print("Player wins")
                exit()
        return

    else:
        print("Cant insert there!")
        position = int(input("Enter new position : "))
        insertLetter(letter, position)


insertLetter('x', 1)
print('one')
insertLetter('x', 2)
print('two')
insertLetter('x', 3)
print('three')
