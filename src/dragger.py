import pygame

from const import *
from board import Board

class Dragger:
    def __init__(self) -> None:
        self.mouseX = 0
        self.mouseY = 0

    def update_mouse(self, position):
        self.mouseX, self.mouseY = position