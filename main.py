from Board import Board
from Player import Player
import pygame

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

WIDTH, HEIGHT = 1000, 800
color = (200, 200, 200)
exit = False

canvas = pygame.display.set_mode((WIDTH, HEIGHT))

Board = Board(HEIGHT, canvas)
Player1 = Player(0)
Player2 = Player(1)

Board.set_players(Player1, Player2)

while not exit:
    canvas.fill(color)
    Board.draw()

    if Board.player2.id:
        p1_text = f'{Board.player1.pieces_left} pieces left'
        p2_text = f'{Board.player2.pieces_left} pieces left'
    else:
        p1_text = f'{Board.player2.pieces_left} pieces left'
        p2_text = f'{Board.player1.pieces_left} pieces left'

    p1_text = myfont.render(
        p1_text, False, (0, 0, 0))
    p2_text = myfont.render(
        p2_text, False, (0, 0, 0))
    canvas.blit(p1_text, (810, 0))
    canvas.blit(p2_text, (810, 750))

    if Board.active_player == Board.player1:
        active_player_top = 200
    else:
        active_player_top = 500

    active_player = myfont.render(
        "Active Player", False, (0, 0, 0))
    canvas.blit(active_player, (810, active_player_top))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if x <= HEIGHT:
                Board.clicked(x, y)

        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
