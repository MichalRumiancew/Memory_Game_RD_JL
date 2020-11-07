import string
import os
import random
from copy import deepcopy

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
    for i in board:
        for m in range(len(board[0])):
            i[m] = random_letters[n]
            n += 1
            m += 1
            if m > len(i):
                m = 0 
            
    return board



def user_input():
    while True:
        coordinates = input("Please provide coordinates, eg. A2 ").upper()
        if len(coordinates) == 2 or len(coordinates) == 3:
            break
        else:
            print("Wrond input, please provide proper coordinates!")

    columns = ord(coordinates[0]) - 65
    if len(coordinates) == 2:
        rows = coordinates[1]
    else:
        rows = coordinates[1]+coordinates[2]

    return (int(rows)-1), int(columns)


def printing_user_input(user_board, computer_board):
    temporary_board = deepcopy(user_board)
    for i in range(2):
        user_cord = user_input()
        temporary_board[user_cord[0]][user_cord[1]] = computer_board[user_cord[0]][user_cord[1]]
        print_board(temporary_board)
    

def comparing_letters(user_input,letters_board):
    pass


def main():
    user_board = init_board()
    computer_board = letters_board(init_board(), random_letters())
    print_board(user_board)
    printing_user_input(user_board, computer_board)
    print_board(user_board)

main()

