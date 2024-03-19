import pygame

from const import *
from board import *
from dragger import Dragger 

class Game():

    def __init__(self) -> None:
        self.board = Board()
        self.dragger = Dragger()
    
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
                    # Check if there's a piece in a square
                    piece = self.board.squares[row][col].piece

                    # If yes, load the img from the assets/images folder, set dimension and
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)

            
