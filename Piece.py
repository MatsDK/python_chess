from prop import get
import pygame
import json

board = open('Assets/board.json',)
board = json.load(board)

offset = open('Assets/offset.json',)
offset = json.load(offset)

image = pygame.image.load("Assets/pieces.png")
image = pygame.transform.scale(image, (600, 200))


class Piece:
    def __init__(self, i, j, player, spacing) -> None:
        self.SPACING = spacing
        self.name = board[j][i]
        self.x = i
        self.y = j
        self.player = player
        self.is_white = bool(player.id)
        self.is_moved = False

    def draw(self, canvas):
        x_offset, y_offset = get(offset, self.name), 0

        if self.is_white != True:
            y_offset = self.SPACING

        cropped_region = (x_offset, y_offset, 100, 100)
        canvas.blit(image, (self.x * self.SPACING,
                    self.y * self.SPACING), cropped_region)

    def get_moves(self, pieces, opponent):
        moves = []

        if self.name == "P":
            moves = self.get_pawn_moves(pieces, opponent)
        if self.name == "N":
            moves = self.get_knight_moves(pieces, opponent)

        return moves

    def get_pawn_moves(self, pieces, opponent):
        moves = []

        if self.is_white:

            if not isinstance(pieces[self.x][self.y - 1], Piece):
                moves.append((self.x, self.y - 1))

                if not self.is_moved and not isinstance(pieces[self.x][self.y - 2], Piece):
                    moves.append((self.x, self.y - 2))

            if (self.x - 1 >= 0 and isinstance(pieces[self.x - 1][self.y - 1], Piece)
                    and pieces[self.x-1][self.y - 1].player == opponent):
                moves.append((self.x - 1, self.y - 1))

            if (self.x + 1 <= 7 and isinstance(pieces[self.x + 1][self.y - 1], Piece)
                    and pieces[self.x+1][self.y - 1].player == opponent):
                moves.append((self.x + 1, self.y - 1))

        else:
            if not isinstance(pieces[self.x][self.y + 1], Piece):
                moves.append((self.x, self.y + 1))

                if not self.is_moved and not isinstance(pieces[self.x][self.y + 2], Piece):
                    moves.append((self.x, self.y + 2))

            if (self.x - 1 >= 0 and isinstance(pieces[self.x - 1][self.y + 1], Piece)
                    and pieces[self.x-1][self.y + 1].player == opponent):
                moves.append((self.x - 1, self.y + 1))

            if (self.x + 1 <= 7 and isinstance(pieces[self.x + 1][self.y + 1], Piece)
                    and pieces[self.x+1][self.y + 1].player == opponent):
                moves.append((self.x + 1, self.y + 1))

        return moves

    def get_knight_moves(self, pieces, opponent):
        moves = []
        directions = [(-2, -1), (-2, 1),  (-1, -2), (-1, 2),
                      (1, -2), (1, 2), (2, -1), (2, 1)]

        for i, j in directions:
            new_x, new_y = self.x + i, self.y + j

            if (new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7):
                if isinstance(pieces[new_x][new_y], Piece):
                    if pieces[new_x][new_y].player == opponent:
                        moves.append((new_x, new_y))
                else:
                    moves.append((new_x, new_y))

        return moves
