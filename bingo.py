
''' 
Program Description:
    This program runs a Bingo game with functionalities to mark numbers and check for wins in different directions. 

Inputs:
    - A nested list representing a Bingo board
    - A list of called numbers

Outputs:
    - Bingo win status messages

Author: Jazlynn Bailey
Date: 10/27/24
'''

def print_bingo():
    print('Bingo found 😀')

def mark_spaces(board, nums):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] in nums or board[row][col] == 'Free':
                board[row][col] = 'X'
    return board

def has_row_bingo(board):
    for row in board:
        if all(space == 'X' for space in row):
            return True
    return False

def has_col_bingo(board):
    for col in range(len(board)):
        if all(board[row][col] == 'X' for row in range(len(board))):
            return True
    return False

def has_diag_topL_botR_bingo(board):
    if all(board[i][i] == 'X' for i in range(len(board))):
        return True
    return False

def has_diag_botL_topR_bingo(board):
    if all(board[i][len(board) - 1 - i] == 'X' for i in range(len(board))):
        return True
    return False

def check_bingo(board):
    wins_cnt = 0
    
    if has_row_bingo(board):
        if wins_cnt == 0:
            print_bingo()
        print("A row is complete!")
        wins_cnt += 1

    if has_col_bingo(board):
        if wins_cnt == 0:
            print_bingo()
        print("A column is complete!")
        wins_cnt += 1

    if has_diag_topL_botR_bingo(board):
        if wins_cnt == 0:
            print_bingo()
        print("A diagonal is complete!")
        wins_cnt += 1

    if has_diag_botL_topR_bingo(board):
        if wins_cnt == 0:
            print_bingo()
        print("A diagonal is complete!")
        wins_cnt += 1

    if wins_cnt == 0:
        print("No Bingo found ☹")


def main():
    board_5x5 = [
        ['Free', 22, 38, 48, 34],
        [39, 'X', 44, 11, 51],
        [27, 62, 'X', 55, 18],
        [19, 42, 73, 'X', 82],
        [66, 90, 17, 89, 'X']
    ]
    
    numbers_called = ['Free', 39, 44, 55, 82]
    
    marked_board = mark_spaces(board_5x5, numbers_called)
    check_bingo(marked_board)

if __name__ == "__main__":
    main()
