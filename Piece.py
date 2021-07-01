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

    def draw(self, canvas):
        x_offset, y_offset = get(offset, self.name), 0

        if self.is_white != True:
            y_offset = self.SPACING

        cropped_region = (x_offset, y_offset, 100, 100)
        canvas.blit(image, (self.x * self.SPACING,
                    self.y * self.SPACING), cropped_region)
