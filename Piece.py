from prop import get
import numpy as np
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

    def get_moves(self, pieces, opponent, check):
        moves = []

        if self.name == "P":
            moves = self.get_pawn_moves(pieces, opponent)
        elif self.name == "N":
            moves = self.get_knight_moves(pieces, opponent)
        elif self.name == "B":
            moves = self.get_bishop_moves(pieces, opponent)
        elif self.name == "R":
            moves = self.get_rook_moves(pieces, opponent)
        elif self.name == "K":
            moves = self.get_king_moves(pieces, opponent, check)
        elif self.name == "Q":
            moves = self.get_queen_moves(pieces, opponent)

        return moves

    def get_moves_with_directions(self, directions, pieces, opponent):
        moves = []

        for x, y in directions:
            for i in range(7):
                new_x, new_y = self.x + (i + 1) * x, self.y + (i + 1) * y

                if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                    if isinstance(pieces[new_x][new_y], Piece):
                        if pieces[new_x][new_y].player == opponent:
                            moves.append((new_x, new_y))

                        break
                    else:
                        moves.append((new_x, new_y))

        return moves

    def get_queen_moves(self, pieces, opponent):
        moves = []
        diag_directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        moves = self.get_moves_with_directions(
            diag_directions, pieces, opponent)
        moves.extend(self.get_moves_with_directions(
            directions, pieces, opponent))

        return moves

    def get_king_moves(self, pieces, opponent, check):
        moves = []
        directions = [(-1, -1), (0, -1), (-1, 1),
                      (1, 1), (0, 1), (-1, 0), (1, -1), (1, 0)]

        for i, j in directions:
            new_x, new_y = self.x + i, self.y + j

            if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                if isinstance(pieces[new_x][new_y], Piece):
                    if pieces[new_x][new_y].player == opponent:
                        moves.append((new_x, new_y))

                else:
                    moves.append((new_x, new_y))

        if not check:
            return moves

        castle_moves = self.get_castle_moves(pieces, opponent)
        self.player.castle_moves = castle_moves
        moves.extend(castle_moves)

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

            if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:

                if isinstance(pieces[new_x][new_y], Piece):
                    if pieces[new_x][new_y].player == opponent:
                        moves.append((new_x, new_y))
                else:
                    moves.append((new_x, new_y))

        return moves

    def get_bishop_moves(self, pieces, opponent):
        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

        return self.get_moves_with_directions(directions, pieces, opponent)

    def get_rook_moves(self, pieces, opponent):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        return self.get_moves_with_directions(directions, pieces, opponent)

    def get_rook_positions(self, pieces):
        positions = []

        for i in range(8):
            for j in range(8):
                if (isinstance(pieces[i][j], Piece) and pieces[i][j].name == "R"
                        and pieces[i][j].player == self.player):
                    positions.append((i, j))

        return positions

    def get_castle_moves(self, pieces, opponent):
        moves = []

        if not self.is_moved:
            rook_positions = self.get_rook_positions(pieces)
            king_pos = self.x, self.y

            if self.player.is_check(pieces, opponent, king_pos):
                return moves

            for i, j in rook_positions:
                isValid = True

                if pieces[i][j].is_moved:
                    continue

                idx, max = sorted([i, self.x])
                curr_idx = idx + 1

                while curr_idx < max:
                    if isinstance(pieces[curr_idx][j], Piece):
                        isValid = False
                        break

                    curr_idx += 1

                if isValid:
                    check_pieces = np.copy(pieces)

                    for new_i in range(2):
                        m = self.x + new_i + 1
                        if i - self.x == -4:
                            m = self.x - new_i - 1

                        check_pieces[m][j] = check_pieces[king_pos[0]][self.y]
                        check_pieces[m][self.y].x, check_pieces[m][self.y].y = m, self.y

                        check_pieces[king_pos[0]][self.y] = 0

                        checked = self.player.is_check(
                            check_pieces, opponent, (m, j))

                        check_pieces[king_pos[0]
                                     ][self.y] = check_pieces[m][self.y]
                        check_pieces[king_pos[0]][self.y].x, check_pieces[king_pos[0]
                                                                          ][self.y].y = king_pos[0], self.y

                        check_pieces[m][j] = 0

                        if checked:
                            isValid = False
                            break

                if isValid:
                    if i - self.x == -4:
                        moves.append((self.x - 2, j))
                    else:
                        moves.append((self.x + 2, j))

        return moves
