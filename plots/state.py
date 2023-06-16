import sys
import pygame
from config import *
from plots.grid import Grid
from trigonometry.circle_mesh import Circle_Mesh
from trigonometry.functions import Functions


class State:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font(None, 40)
        self.clock = pygame.time.Clock()
        self.new_state()

    def new_state(self):
        self.grid = Grid(self)
        self.circle_mesh = Circle_Mesh(self)
        self.functions = Functions(self)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.functions.update()

        pygame.display.flip()
        self.clock.tick(fps)
        pygame.display.set_caption(f"{caption}")

    def draw_txt(self):
        if len(self.functions.values) > 0:
            sin_txt = self.font.render(f'sin:{round(self.functions.values[-1][1], 2)} ', True, red_dark)
            cos_txt = self.font.render(f'cos:{round(self.functions.values[-1][2], 2)} ', True, blue_dark)
            self.screen.blit(sin_txt, (WIDTH - WIDTH // 4 + 10, 40))
            self.screen.blit(cos_txt, (WIDTH - WIDTH // 4 + 10, 60))

    def draw(self):
        self.screen.fill(white)
        self.circle_mesh.draw()
        self.grid.draw()
        self.functions.draw()
        self.draw_txt()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.check_event()

