import pygame
from config import *


class Grid:
    def __init__(self, game):
        self.game = game

    # grid lines
    def draw(self):
        # y line
        pygame.draw.line(self.game.screen, black,
                         y_a, y_b,
                         2)
        # x line
        pygame.draw.line(self.game.screen, black,
                         x_a, x_b,
                         2)

        # dividing line
        pygame.draw.line(self.game.screen, gray_w,
                         d_a, d_b,
                         10)
