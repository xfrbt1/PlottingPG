import sys
import pygame
from config import *
from plots.grid import Grid
from trygonometry.circle_mesh import Circle_Mesh
from trygonometry.functions import Functions


class State:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

    def draw(self):
        self.screen.fill(white)
        self.circle_mesh.draw()
        self.grid.draw()
        self.functions.draw()


    def run(self):
        while True:
            self.update()
            self.draw()
            self.check_event()

