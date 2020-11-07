import string
import os

def init_board(rows=5, columns=5):

    board = []
    for column in range(rows):
        board.append(['*'] * columns)

    return board


def print_board(board):
    
    upper_case_abc = string.ascii_uppercase
    n = 1
    print()
    print("  "+" ".join(upper_case_abc[:len(board[0])]))
    for row in board:
        print(f'{n} {" ".join(row)}')
        n += 1

        
print_board(init_board())

