import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
        pygame.display.set_caption('Chess')
        self.game = Game()
        

    def mainloop(self):
        while True:
            self.game.show_bg(self.screen)
            self.game.show_pieces(self.screen)
            dragger = self.game.dragger

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN: # click
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if self.game.board.squares[clicked_row][clicked_col].has_piece():
                        piece = self.game.board.squares[clicked_row][clicked_col].piece
                        


                elif event.type == pygame.MOUSEMOTION: # mouse motion
                    pass

                elif event.type == pygame.MOUSEBUTTONUP: # Mouse releas
                    pass

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()