from config import *
import pygame
import math


class Functions:
    def __init__(self, game):
        self.game = game
        self.angle = ANGLE

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= 0.01
            print(self.angle)

        if keys[pygame.K_RIGHT]:
            self.angle += 0.01
            print(self.angle)

    def draw_hypotenuse(self):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        ab = WIDTH-(WIDTH // 4) + (RADIUS * cos_a)
        ac = HEIGHT // 2 + (RADIUS * sin_a)

        pygame.draw.line(self.game.screen, green,
                         circle_centre,
                         [ab, ac], 2)

        pygame.draw.circle(self.game.screen, green,
                           circle_centre, 4)

        pygame.draw.circle(self.game.screen, green,
                           (ab, ac), 5)

    def draw_x_projection(self):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        ab = WIDTH-(WIDTH // 4) + (RADIUS * cos_a)
        ac = HEIGHT // 2 + (RADIUS * sin_a)

        pygame.draw.line(self.game.screen, blue,
                         circle_centre,
                         [ab, (HEIGHT // 2)], 4)

        pygame.draw.circle(self.game.screen, blue,
                           (ab, HEIGHT // 2), 5)

        pygame.draw.line(self.game.screen, blue,
                         [ab, ac],
                         [ab, HEIGHT//2], 2)

    def draw_y_projection(self):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        ab = WIDTH-(WIDTH // 4) + (RADIUS * cos_a)
        ac = HEIGHT // 2 + (RADIUS * sin_a)

        pygame.draw.line(self.game.screen, red,
                         circle_centre,
                         [WIDTH-(WIDTH//4), ac], 4)

        pygame.draw.circle(self.game.screen, red,
                           (WIDTH-(WIDTH//4), ac), 5)

        pygame.draw.line(self.game.screen, red,
                         [ab, ac],
                         [WIDTH-(WIDTH//4), ac], 2)

    def draw(self):
        self.draw_x_projection()
        self.draw_y_projection()
        self.draw_hypotenuse()
