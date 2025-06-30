from position import Position
from move import Move
class Board:
    def __init__(self,grid = None):
        if grid is None:
            self.initialize_board()
        else: 
            self.grid = grid
    
    def initialize_board(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
   
    def print_board(self):
        """only using when gui is not implemented"""
        for i in self.grid:
            print(i)
    def get_piece(self, pos:Position):
        """gets the piece of a specific position"""
        return self.grid[pos.row][pos.col]
    def move_piece(self,move:Move ):
        pass
