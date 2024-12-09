import pygame
import sys
from pieces import *


def initialize_board():
    # Initialize an 8x8 board with None
    board = [[None for _ in range(8)] for _ in range(8)]
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == 1 or row == 6:
                board[row][col] = Pawn(row,col,'P')
                print(board[row][col])
    return board
def update_board(screen, board, square_size=80):
    colors = [(255, 255, 255), (0, 0, 0)]  # White and Black
    font = pygame.font.Font(None, 60)  # Font for rendering text

    for row in range(len(board)):
        for col in range(len(board[row])):
            # Draw the square
            color = colors[(row + col) % 2]
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, color, rect)

            # Draw the piece, if any
            piece = board[row][col]
            if piece:
                text = font.render(piece.symbol, True, (255, 0, 0))  # Red "P" for Pawn
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)


def main():
    pygame.init()
    board_size = 8
    square_size = 80  
    screen_width = board_size * square_size
    screen_height = board_size * square_size
    screen = pygame.display.set_mode((screen_width, screen_height))

    board = initialize_board()
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the chessboard
        screen.fill((0, 0, 0))
        #draw_chessboard(screen, board, square_size)
        update_board(screen, board, square_size)

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()