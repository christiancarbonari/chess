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

            if dragger.dragging:
                dragger.update_blit(self.screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN: # click
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if self.game.board.squares[clicked_row][clicked_col].has_piece():
                        piece = self.game.board.squares[clicked_row][clicked_col].piece
                        self.game.board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        # show methods
                        self.game.show_bg(self.screen)                        
                        self.game.show_moves(self.screen)
                        self.game.show_pieces(self.screen)


                elif event.type == pygame.MOUSEMOTION: # mouse motion
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        self.game.show_bg(self.screen)
                        self.game.show_moves(self.screen)
                        self.game.show_pieces(self.screen)                        
                        dragger.update_blit(self.screen)

                elif event.type == pygame.MOUSEBUTTONUP: # Mouse release
                    dragger.undrag_piece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

            # Added a comment here

            # Here I would like to add a lot of things!!!

            # I added a comment here


main = Main()
main.mainloop()