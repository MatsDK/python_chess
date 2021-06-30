import pygame

Color_line = (80, 80, 80)


class Board:
    def __init__(self, SPACING) -> None:
        self.SPACING = SPACING

    def display(self, canvas):
        for i in range(8):
            for j in range(8):

                if (i % 2) == 0 and (j % 2) == 0:
                    pygame.draw.rect(canvas, Color_line, pygame.Rect(
                        i * self.SPACING, j * self.SPACING, i + self.SPACING, j + self.SPACING))
                elif (i % 2) == 1 and (j % 2) == 1:
                    pygame.draw.rect(canvas, Color_line, pygame.Rect(
                        i * self.SPACING, j * self.SPACING, i + self.SPACING, j + self.SPACING))
