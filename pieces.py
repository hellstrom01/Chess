class Piece:
    def __init__(self,x,y,symbol,color):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color = color

class Pawn(Piece):
    def __init__(self,x,y,symbol,color,points = 1):
        super().__init__(x,y,symbol,color) 
        self.points = points
        
    def legal_move():
        legal = [self.x -1,self.y]
        return legal