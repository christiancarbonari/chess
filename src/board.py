from const import *
from square import Square

class Board:

    def __init__(self) -> None:
        self.squares = [[0,0,0,0,0,0,0,0] for cols in range(COLS)]
        self._create()

    def _create(self):       

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):

        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)
        print(row_pawn, row_other)

 