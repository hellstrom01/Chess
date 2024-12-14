import pygame
import sys
import os
from pieces import *
from gamelogic import Game, GameLogic

def main():
    pygame.init()
    board_size = 8
    square_size = 80  
    screen_width = board_size * square_size
    screen_height = board_size * square_size
    screen = pygame.display.set_mode((screen_width, screen_height))
    game = Game()
    board = game.initialize_board()
    player1 = GameLogic( board,game.player_white_pieces)
    player2 = GameLogic( board,game.player_black_pieces)
    counter = 0 # player 1 ( white) turn at odd number
    # Main loop
    black_pawn = pygame.image.load(os.getcwd() + "/PawnPictures/black-pawn.png").convert_alpha()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                        # Handle mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                row, col = mouse_y // square_size, mouse_x // square_size
                piece = board[row][col]
                if piece:  # If a piece is clicked
                    game.selected_piece = piece
                    game.dragging = True
                    game.original_position = (row, col)

            if event.type == pygame.MOUSEMOTION and game.dragging:
                mouse_x, mouse_y = event.pos
                game.selected_piece.row = mouse_y - square_size // 2
                game.selected_piece.col = mouse_x - square_size // 2

            if event.type == pygame.MOUSEBUTTONUP and game.dragging:
                mouse_x, mouse_y = event.pos
                new_row, new_col = mouse_y // square_size, mouse_x // square_size
                
                # Validate and update the piece's position
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    old_row, old_col = game.original_position
                    board[old_row][old_col] = None
                    board[new_row][new_col] = game.selected_piece
                    game.selected_piece.row, game.selected_piece.col = new_row, new_col
                
                # Reset dragging state
                game.selected_piece = None
                game.dragging = False
                game.original_position = None


        # Draw the chessboard
        screen.fill((0, 0, 0))
        #draw_chessboard(screen, board, square_size)
        if counter %2 == 1:
            player1.make_move(board, "player1")
            game.update_board(screen, board, black_pawn)
            print(game.player_black_pieces)
            counter +=1
        else:
            player2.make_move(board, player2)
            game.update_board(screen, board, black_pawn)
            counter +=1      
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()