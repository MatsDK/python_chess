from Piece import Piece
import pygame

Color = (80, 80, 80)
Highlight_color = (0, 140, 240)


class Board:
    def __init__(self, HEIGHT, canvas) -> None:
        self.HEIGHT = HEIGHT
        self.SPACING = int(HEIGHT/8)
        self.canvas = canvas
        self.highlighted = [[0 for i in range(8)] for j in range(8)]
        self.pieces = [[0 for i in range(8)] for j in range(8)]
        self.selected = False

    def remove_selected(self):
        self.highlighted = [[0 for i in range(8)] for j in range(8)]
        self.selected = False

    def draw(self):
        for i in range(8):
            for j in range(8):

                if (i % 2) == 0 and (j % 2) == 1:
                    pygame.draw.rect(self.canvas, Color, pygame.Rect(
                        i * self.SPACING, j * self.SPACING,  self.SPACING,  self.SPACING))
                if (i % 2) == 1 and (j % 2) == 0:
                    pygame.draw.rect(self.canvas, Color, pygame.Rect(
                        i * self.SPACING, j * self.SPACING, self.SPACING,  self.SPACING))

                if bool(self.highlighted[i][j]):
                    pygame.draw.rect(self.canvas, Highlight_color, pygame.Rect(
                        i * self.SPACING, j * self.SPACING, self.SPACING,  self.SPACING))

                if isinstance(self.pieces[i][j], Piece):
                    self.pieces[i][j].draw(self.canvas)

        pygame.draw.line(self.canvas, Color, (self.HEIGHT, 0),
                         (self.HEIGHT, self.HEIGHT), 2)

    def set_players(self, player1, player2):
        self.player1, self.player2 = player1, player2

        if player1.id == 1:
            self.active_player = player1
        else:
            self.active_player = player2

        self.set_pieces()

    def set_pieces(self):

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
        x, y = x // self.SPACING, y // self.SPACING

        # toggle if piece is selected
        if self.selected != False and self.pieces[x][y] == self.selected:
            return self.remove_selected()

        # if clicked on piece of active_player set selected
        if isinstance(self.pieces[x][y], Piece) and self.pieces[x][y].player == self.active_player:
            self.highlighted = [[0 for i in range(8)] for j in range(8)]
            self.highlighted[x][y] = 1

            self.selected = self.pieces[x][y]

            moves = []
            if self.active_player == self.player2:
                moves = self.selected.get_moves(self.pieces, self.player1)
            else:
                moves = self.selected.get_moves(self.pieces, self.player2)

            for i, j in moves:
                self.highlighted[i][j] = 1

        # if not clicked on own piece, move the piece
        elif self.selected != False:
            if self.highlighted[x][y]:
                self.move(self.selected.x, self.selected.y, x, y)

    def move(self, x1, y1, x2, y2):
        self.selected.x, self.selected.y = x2, y2
        self.pieces[x2][y2] = self.selected
        self.pieces[x2][y2].is_moved = True

        self.pieces[x1][y1] = 0

        self.remove_selected()
        self.next_player()

    def next_player(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1
