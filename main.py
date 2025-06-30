from color import Color
from board import Board
def choose_c(c: Color):
    print(" you choose color ", c.value)

def b():
    b = Board()
    print(b.print_board())
    b.get_piece(1,2)
b()