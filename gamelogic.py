import pygame
from pieces import Pawn
class Game:
    def __init__(self):
        self.player_black_pieces = {}
        self.player_white_pieces = {}
        self.board = [[None for _ in range(8)] for _ in range(8)] 
        self.selected_piece = None
        self.dragging = False
        self.original_position = None
    
    def get_board(self):
        return self.board
    def get_player_1_pieces(self):
        return self.player_white_pieces
    def get_player_2_pieces(self):
        return self.player_black_pieces

    def initialize_board(self):
        # Initialize an 8x8 board with None
        # row is the x coordinate, col is the x 
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if row == 1:
                    self.board[row][col] = Pawn(row,col,'P',"black")
                    try:
                        self.player_black_pieces['pawns'].append([row,col])
                    except KeyError:
                        self.player_black_pieces['pawns'] = [[row,col]]

        return self.board

    def update_board(self,screen, board,black_pawn, square_size=80):
        colors = [(255, 255, 255), (100,40,0)]  # White and Brown
        font = pygame.font.Font(None, 60)  # Font for rendering text
        for row in range(len(board)):
            for col in range(len(board[row])):
                # Draw the square
                color = colors[(row + col) % 2]
                rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
                pygame.draw.rect(screen, color, rect)

                                # Draw the piece, if any
                piece = board[row][col]
                if piece and piece != self.selected_piece:
                    if piece.color == 'black':
                        pawn_image = black_pawn
                    else:
                        pass
                    pawn_image = pygame.transform.scale(pawn_image, (square_size, square_size))
                    screen.blit(pawn_image, (col * square_size, row * square_size))

                    # Draw the dragged piece on top
        if self.dragging and self.selected_piece:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pawn_image = black_pawn
            pawn_image = pygame.transform.scale(pawn_image, (square_size, square_size))
            screen.blit(pawn_image, (mouse_x - square_size // 2, mouse_y - square_size // 2))
class GameLogic(Game):
    def __init__(self,board,player_pieces):
        super().__init__()
        self.board = board
        self.player = player_pieces


    def make_move(self,board,player):
        if player == "player1":
             pieces_position =self.get_player_1_pieces()
             print(pieces_position)
        pass
