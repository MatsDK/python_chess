from prop import get
import pygame
import json

data = open('Assets/data.json',)
data = json.load(data)

data1 = open('Assets/data1.json',)
data1 = json.load(data1)

image = pygame.image.load("Assets/pieces1.png")
image = pygame.transform.scale(image, (600, 200))


class Piece:
    def __init__(self, i, j, player, spacing) -> None:
        self.SPACING = spacing
        self.name = data[j][i]
        self.x = i
        self.y = j
        self.player = player
        self.is_white = bool(player.id)

    def draw(self, canvas):
        x_offset, y_offset = get(data1, self.name), 0

        if self.is_white is not True:
            y_offset = self.SPACING

        cropped_region = (x_offset, y_offset, 100, 100)
        canvas.blit(image, (self.x * self.SPACING,
                    self.y * self.SPACING), cropped_region)
