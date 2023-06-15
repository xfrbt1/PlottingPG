from config import *
import pygame


class Circle_Mesh:
    def __init__(self, game):
        self.game = game

    def draw(self):

        pygame.draw.line(self.game.screen, black,
                         yc_b,
                         yc_a, 3)

        pygame.draw.circle(self.game.screen, gray_b,
                           circle_centre, RADIUS, 5)

