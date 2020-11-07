import string

def init_board(rows=5, columns=5):

    board = []
    for column in range(rows):
        board.append(['*'] * columns)

    return board


def print_board(board):
    
    upper_case_abc = list(string.ascii_uppercase)
    n = 1
    first_str = ''
    for row in board:
        print(f'{n} {row}')
        n += 1

        
print_board(init_board())