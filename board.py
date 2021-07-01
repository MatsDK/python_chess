from pygame.constants import CONTROLLER_BUTTON_GUIDE
from Piece import Piece
import pygame

Color_line = (80, 80, 80)


class Board:
    def __init__(self, HEIGHT, canvas) -> None:
        self.HEIGHT = HEIGHT
        self.SPACING = int(HEIGHT/8)
        self.canvas = canvas
        self.highlighted = []
        self.pieces = []

    def update(self):

        for i in range(8):
            for j in range(8):

                if (i % 2) == 0 and (j % 2) == 1:
                    pygame.draw.rect(self.canvas, Color_line, pygame.Rect(
                        i * self.SPACING, j * self.SPACING,  self.SPACING,  self.SPACING))
                if (i % 2) == 1 and (j % 2) == 0:
                    pygame.draw.rect(self.canvas, Color_line, pygame.Rect(
                        i * self.SPACING, j * self.SPACING, self.SPACING,  self.SPACING))

                if isinstance(self.pieces[i][j], Piece):
                    self.pieces[i][j].draw(self.canvas)

        pygame.draw.line(self.canvas, Color_line, (self.HEIGHT, 0),
                         (self.HEIGHT, self.HEIGHT), 2)

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        if player1.id == 1:
            self.active_player = player1
        else:
            self.active_player = player2

        self.set_pieces()

    def set_pieces(self):

        self.pieces = [[0 for i in range(8)] for j in range(8)]

        for i in range(8):
            for j in range(8):
                if j == 0 or j == 1:
                    if self.player1.id == 0:
                        self.pieces[i][j] = Piece(
                            i, j, self.player1, self.SPACING)
                    else:
                        self.pieces[i][j] = Piece(
                            i, j, self.player2, self.SPACING)
                elif j == 6 or j == 7:
                    self.pieces[i][j] = Piece(
                        i, j, self.active_player, self.SPACING)

    def clicked(self, x, y):
        x, y = x//self.SPACING, y // self.SPACING
        if isinstance(self.pieces[x][y], Piece):
            print(self.pieces[x][y].name)
            print(self.active_player == self.pieces[x][y].player)
            self.highlighted = [(x, y)]
