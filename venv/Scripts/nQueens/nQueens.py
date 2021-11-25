import numpy as np
import copy

columns = []

"""
ex3 =====================================================
Forward Checking build recursive func that use a three func
1) next_move - place 1 in threat places,
2)notLegal- after we now the threat's board we can check if the position  legal.
3) display to present the board  
"""


def next_move(board, col, row):
    # board[row:,col] = 1
    for i in range(board.shape[0]):
        board[i][col] = 1
        for j in range(board.shape[0]):
            if ((i - col) == (row - j)) or ((i + col) == (row + j)):
                board[i][j] = 1


def display():
    print("I did it! Here is my solution")
    for i in range(len(columns)):
        for j in range(n):
            if j == columns[i]:
                print('♛', end=' ')
            else:
                print(' +', end=' ')
        print()
    print(columns)


def notLegal(bor, row):
    for i in range(row, n):
        if 0 not in bor[i, :]:
            return True
    return False


def queen_solved(board, row=0):
    if (n == row):  # stop condition
        return True
    if notLegal(board, row):  # and if its legal we do Forward Checking
        return False
    nBoard = copy.deepcopy(board)
    for i in range(n):
        if nBoard[row][i] == 1:  # for all new queen position we check if is a legal place
            continue
        next_move(nBoard, i, row)
        result = queen_solved(nBoard, row + 1)  # recorsive
        if not result:
            nBoard = board  # if board not legal we back state
        if result:
            columns.append(i)
            return True
    return False


n = 7
x = np.zeros((n, n))
queen_solved(x)
display()

"""
ex4 =============================
I success to n=100, I belive its ,can to be more
[41, 56, 94, 28, 30, 38, 87, 74, 53, 58, 39, 14, 77, 34, 72, 51, 4, 33, 55, 21, 48, 6,
 88, 29, 97, 82, 79, 49, 36, 42, 84, 43, 66, 73, 12, 7, 92, 0, 47, 23, 71, 18, 62, 86,
 91, 11, 70, 40, 15, 31, 67, 3, 90, 24, 37, 10, 75, 99, 57, 64, 83, 93, 22, 59, 68, 5,
 52, 16, 44, 50, 80, 98, 25, 63, 81, 26, 19, 2, 35, 20, 60, 45, 8, 17, 76, 96, 61, 46,
32, 89, 13, 1, 54, 9, 85, 69, 65, 27, 95, 78]
queen_stochasty get numpay array size n*n and num of row with Default 0
it's recorsive func. to measure the iter only in true we add 1  

"""

import random

iter = []


def queen_stochasty(board, row=0):
    if (n == row):  # stop condition
        iter.append(1)
        return True
    if notLegal(board, row):  # and if its legal we do Forward Checking
        return False
    nBoard = copy.deepcopy(board)
    while 0 in board[row, :]:
        i = random.randrange(n)
        if nBoard[row][i] == 1:  # for all new queen position we check if is a legal place
            continue
        next_move(nBoard, i, row)
        result = queen_stochasty(nBoard, row + 1)  # recorsive
        if not result:
            nBoard = board  # if board not legal we back state
            nBoard[row][i] = 1
        if result:
            columns.append(i)
            iter.append(1)
            return True
    return False


"""
average of iter in board 15*15 in stuchasti 906.05
"""


def average(n):  # average of iter in board 15*15 in stuchsti 906.05
    sum = 0
    for i in range(20):
        x = np.zeros((n, n))
        queen_stochasty(x, 0)
        #
        sum += len(iter)
    print('average of iter in board n*n in stuchsti', sum / 20)
