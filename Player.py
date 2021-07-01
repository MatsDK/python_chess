class Player:
    def __init__(self, board, id) -> None:
        self.id = id
        self.moves = 0
        self.pieces = []
        self.board = board
