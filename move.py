from position import Position
from piece import Piece
class Move:
    def __init__(self, from_pos:Position,to_pos:Position, captured:Piece):
        self.from_pos = from_pos
        self.to_pos = to_pos
        self.captured = None