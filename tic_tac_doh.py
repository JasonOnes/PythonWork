"""determines the winner of any given tic tac toe game"""


def find_win(y):
    z = 0
    n = 0
    while n < len(y):
        for x in y:
            if y[n][z] == y[n][z+1] and y[n][z] == y[n][z+2]:
                print("winner")
            else:
                pass
            n += 1

def diag(y):
    z = 0
    n = 0
    while n < len(y) and z < len(y):
        if y[n][z] == y[n+1][z+1] and y[n][z] == y[n+2][z+2]:
            print("winner")
        elif y[len(y)][z] == y[len(y)-1][z] and y[len(y)][z] == y[len(y)-2][z]:
            print("winner")


def tic_win(board):
    find_win(board)
    column = list(zip(*board))
    find_win(column)
    diag(board)
    

    """x = len(board)
    n = 0
    column = list(zip(*board))

    while n < x:
        for row in board[n]:
            if (board[n][0] == board[n][1]) and (board[n][0] == board[n][2]):
                print("winner")
            else:
                pass
        n += 1
    while n < x:
        for col in column[n]:
            if (column[n][0] == column[n][1]) and (column[n][0] == column[n][2]):
                print("winner")
            else:
                pass
        n +=1

    if board[0][0] == board[1][1] and board[0][0]== board[2][2]:
        print("winner")
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        print("winner")
"""
board_1 = [[1, 1, 1],
           [0, 0, 1],
           [0, 1, 0]]

tic_win(board_1)
