class Piece:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Pawn(Piece):
    def __init__(self,x,y,symbol,points = 1):
        super().__init__(x,y)
        self.symbol = symbol
        self.points = points
    def legal_move():
        pass