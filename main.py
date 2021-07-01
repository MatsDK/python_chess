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
Player1 = Player(Board, 1)
Player2 = Player(Board, 0)

Board.set_players(Player1, Player2)

image = pygame.image.load("Assets/pieces1.png")
image = pygame.transform.scale(image, (600, 200))


exit = False

while not exit:
    canvas.fill(color)

    Board.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if x <= HEIGHT:
                Board.clicked(x, y)

        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()

# K [20, 20, 100, 100] Q [188, 20, 100,100] R [358, 20, 100, 100]
# B [526, 20, 100, 100] N [692, 20, 100,100] P [861, 20, 100, 100]

# K [20, 164, 100, 100] Q [188, 164, 100,100] R [358, 164, 100, 100]
# B [526, 164, 100, 100] N [692, 164, 100,100] P [861, 164, 100, 100]
