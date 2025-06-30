from abc import ABC, abstractmethod
from color import Color
from position import Position
class piece(ABC):
    def __init__(self, color:Color,pos:Position):
        self.color = color
        self.pos = pos
    @abstractmethod
    def get_valid_moves(self):
        pass

class pawn(piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
    def get_valid_moves(self):
        if self.color == Color.WHITE:
            if self.first_move(self):
                return [self.pos.row+2]
            return [self.pos.row+1]
        else:
            if self.first_move():
                return [self.pos.row+2]
             
            return [self.pos.row-1]
    def first_move(self):
        if self.color == Color.WHITE:
            if self.row.pos == 1:
                return True
            return False
        else:
            if self.row.pos == 6:
                return True
            return False


class king(piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
    def get_valid_moves(self):
        if self.color == Color.WHITE:
            return [self.pos.row+1]
        else: 
            return [self.pos.row-1]