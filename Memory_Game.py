import string
import os
import random

def init_board(rows=3, columns=4):

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

    
def random_letters(rows = 3, columns=4):
    lower_case_abc = list(string.ascii_lowercase)
    abc_list = []
    for i in range((rows*columns)//2):
        abc_list.append(lower_case_abc[i]*2)

    abc_str = ''.join(abc_list)
    abc_list_2 = list(abc_str)
    random.shuffle(abc_list_2)

    return abc_list_2


def letters_board(board, random_letters):
    n = 0 
    m = 0
    for i in board[0]:
        i[m] = random_letters[n]
        n += 1
        m += 1
        

    return board

print_board(letters_board(init_board(), random_letters()))