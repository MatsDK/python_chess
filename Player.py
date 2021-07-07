from numpy.lib.arraysetops import isin
from Piece import Piece
import numpy as np


class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.pieces_left = 16

    def is_check(self, pieces, opponent):
        king_pos = False

        for i in range(8):
            for j in range(8):
                if (isinstance(pieces[i][j], Piece) and pieces[i][j].name == "K"
                        and pieces[i][j].player == self):
                    king_pos = (i, j)

        attacks = []

        for i in range(8):
            for j in range(8):
                if isinstance(pieces[i][j], Piece) and pieces[i][j].player == opponent:
                    if king_pos and (king_pos in pieces[i][j].get_moves(pieces, self)):
                        attacks.append((i, j))

        return bool(len(attacks))

    def is_check_mate(self, pieces, opponent):

        if not self.is_check(pieces, opponent):
            return False

        check_pieces = np.copy(pieces)

        for i in range(8):
            for j in range(8):
                if isinstance(check_pieces[i][j], Piece) and check_pieces[i][j].player == self:
                    moves = check_pieces[i][j].get_moves(
                        check_pieces, opponent)

                    for new_i, new_j in moves:
                        check_pieces[new_i][new_j] = check_pieces[i][j]
                        check_pieces[new_i][new_j].x, check_pieces[new_i][new_j].y = new_i, new_j

                        check_pieces[i][j] = 0

                        checked = self.is_check(check_pieces, opponent)

                        check_pieces[i][j] = check_pieces[new_i][new_j]
                        check_pieces[i][j].x, check_pieces[i][j] = i, j

                        check_pieces[new_i][new_j] = 0 

                        if not checked:
                            return False

        return True
