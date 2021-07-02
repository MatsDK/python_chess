from Board import Board
from Player import Player
import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 800
PIECE_W = 144
PIECE_M = 28
color = (200, 200, 200)
Color_line = (80, 80, 80)

canvas = pygame.display.set_mode((WIDTH, HEIGHT))

Board = Board(HEIGHT, canvas)
Player1 = Player(Board, 0)
Player2 = Player(Board, 1)

Board.set_players(Player1, Player2)

exit = False

while not exit:
    canvas.fill(color)

    Board.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if x <= HEIGHT:
                Board.clicked(x, y)

        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
