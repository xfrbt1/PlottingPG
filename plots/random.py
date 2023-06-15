import random

import pygame
from config import *


class Random_Function:
    def __init__(self, game):
        self.game = game
        self.values_list = list()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            xr = random.randint(WIDTH//10, WIDTH)
            yr = random.randint(0, HEIGHT-(HEIGHT // 10))
            self.values_list.append([xr, yr])
            print(xr, yr)

    def draw(self):
        for i in self.values_list:
            pygame.draw.circle(self.game.screen, red,
                               (i[0], i[1]), 3)
