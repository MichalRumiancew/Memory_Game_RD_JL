import string
import os
import rando

def init_board(rows=5, columns=5):

    board = []
    for column in range(rows):
        board.append(['*'] * columns)

    return board


def print_board(board):
    
    upper_case_abc = string.ascii_uppercase
    n = 1
    print()
    print("   "+" ".join(upper_case_abc[:len(board[0])]))
    for row in board:
        print(f'{n:<2} {" ".join(row)}')
        n += 1

        
print_board(init_board(10,5))


def random_letters(row, col):
    for i in range(row*col)
    for i in range(len(board)):
        random_tab = []
        for i in range(len(board[0])):
            random_tab.append()



