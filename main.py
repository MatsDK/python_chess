from board import Board
import pygame

pygame.init()

WIDTH = 800
color = (255, 255, 255)
Color_line = (80, 80, 80)
SPACING = int(WIDTH / 8)

canvas = pygame.display.set_mode((WIDTH, WIDTH))

Board = Board(SPACING)

exit = False

while not exit:
    canvas.fill(color)

    Board.display(canvas)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
