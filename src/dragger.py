import pygame

from const import *
from board import Board

class Dragger:
    def __init__(self) -> None:
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self, surface, sizes=128):
        self.piece.set_texture(size=sizes)
        texture = self.piece.texture

        img = pygame.image.load(texture)

        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_center)
        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, position):
        self.mouseX, self.mouseY = position

    def save_initial(self, position):
        self.initial_row = position[1] // SQSIZE
        self.initial_rcol = position[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
    
    def save_final(self):
        pass


