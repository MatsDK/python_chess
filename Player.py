from Piece import Piece


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

        if not king_pos: 
            return False

        for i in range(8):
            for j in range(8):
                if isinstance(pieces[i][j], Piece) and pieces[i][j].player == opponent:
                    if(king_pos in pieces[i][j].get_moves(pieces, self)):
                        attacks.append((i, j))

        return bool(len(attacks))
