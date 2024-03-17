import pygame

from const import *
from board import *

class Game():

    def __init__(self) -> None:
        self.board = Board()
    
    # Show methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0: 
                    color = (234,235,200) # Light Green
                else:
                    color = (119, 154, 88) # Dark Green

                rect = ( col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    pass
