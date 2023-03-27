import numpy as np


ROWS, COLS = 6, 7

def make_board():
    board = np.zeros((ROWS,COLS))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def iVL(board, col):
    return board[ROWS-1][col] == 0

def gEX(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r
        
def printB(board):
    print(np.flip(board, 0))

def wM(board, piece):
    # Check Horizontals
    for c in range(COLS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Check Verticals
    for c in range(COLS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check Positive Diags
    for c in range(COLS-3):
        for r in range(ROWS -3):
             if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Check Negative Diags
    for c in range(COLS-3):
        for r in range(3, ROWS):
             if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
board = make_board()
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6): "))
        if iVL(board, col):
            row = gEX(board, col)
            drop_piece(board, row, col, 1)
            if wM(board, 1):
                print("Player 1 Wins")
                game_over = True
                break
    # Ask for player 2 input
    else:
        col = int(input("Player 2 Make your selection (0-6): "))
        if iVL(board, col):
            row = gEX(board, col)
            drop_piece(board, row, col, 2)
            if wM(board, 2):
                print("Player 2 Wins")
                game_over = True
                break
    printB(board)
    turn += 1
    turn = turn % 2 