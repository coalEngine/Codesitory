import numpy as np
import pygame as pg
import sys, math

ROWS, COLS = 6, 7
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def make_board():
    # Creates an array of 0s which becomes the board
    board = np.zeros((ROWS,COLS))
    return board

def drop_piece(board, row, col, piece):
    # Drops the Piece in the selected row
    board[row][col] = piece

def iVL(board, col):
    # Gives the illusion of the piece dropping, into a row
    return board[ROWS-1][col] == 0

def gEX(board, col):
    # Checks if a certain square is empty and if it is, return the number row its on
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
            
def drawBoard(board):
    for c in range(COLS):
        for r in range(ROWS):
            pg.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pg.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pg.draw.circle(screen, BLUE, (int(c*SQUARESIZE+SQUARESIZE/2), height -int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pg.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pg.display.update()
    
    
board = make_board()
game_over = False
turn = 0
pg.init()

SQUARESIZE= 100
width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pg.display.set_mode(size)

screen.fill(WHITE)
pg.display.set_caption("Connect 4")
drawBoard(board)
pg.display.update()

myFont = pg.font.SysFont('Dogica Pixel', 40)

while not game_over:
    for evt in pg.event.get():
        if evt.type == pg.QUIT:
             sys.exit()
        if evt.type == pg.MOUSEMOTION:
            pg.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = evt.pos[0]
            if turn == 0:
                pg.draw.circle(screen, BLUE, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pg.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
        pg.display.update()
        if evt.type == pg.MOUSEBUTTONDOWN:
            pg.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # Ask for player 1 input        
            if turn == 0:
                posx = evt.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if iVL(board, col):
                    row = gEX(board, col)
                    drop_piece(board, row, col, 1)
                    if wM(board, 1):
                        label = myFont.render('Player 1 Wins!', 1, BLUE)
                        screen.blit(label, (110, 40))
                        game_over = True
                       
            # Ask for player 2 input
            else:
                posx = evt.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if iVL(board, col):
                    row = gEX(board, col)
                    drop_piece(board, row, col, 2)
                    if wM(board, 2):
                        label = myFont.render('Player 2 Wins!', 1, RED)
                        screen.blit(label, (110, 40))
                        game_over = True
            printB(board)
            drawBoard(board)
            turn += 1
            turn = turn % 2 
            if game_over:
                pg.time.wait(3000)
            
