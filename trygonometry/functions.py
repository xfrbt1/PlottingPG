from config import *
import pygame
import math


class Functions:
    def __init__(self, game):
        self.game = game

        self.angle = ANGLE
        self.values = list()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle += 0.01
            print("angle ", self.angle)
            print("sin ", math.sin(self.angle))
            print("cos ", math.cos(self.angle))
            self.values.append([self.angle, math.sin(self.angle), math.cos(self.angle)])

        if keys[pygame.K_RIGHT]:
            self.angle -= 0.01
            print("angle ", self.angle)
            print("sin ", math.sin(self.angle))
            print("cos ", math.cos(self.angle))
            self.values.append([self.angle, math.sin(self.angle), math.cos(self.angle)])

    def draw_hypotenuse(self):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        ab = WIDTH - (WIDTH // 4) + (RADIUS * cos_a)
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

        ab = WIDTH - (WIDTH // 4) + (RADIUS * cos_a)
        ac = HEIGHT // 2 + (RADIUS * sin_a)

        pygame.draw.line(self.game.screen, blue,
                         circle_centre,
                         [ab, (HEIGHT // 2)], 4)

        pygame.draw.circle(self.game.screen, blue,
                           (ab, HEIGHT // 2), 5)

        pygame.draw.line(self.game.screen, blue,
                         [ab, ac],
                         [ab, HEIGHT // 2], 2)

        if len(self.values) > 0:
            pygame.draw.line(self.game.screen, blue,
                             [ab, HEIGHT//2],
                             [WIDTH - WIDTH // 4 + self.values[-1][2] * RADIUS, HEIGHT + self.values[-1][0] * 10],
                             1)

    def draw_y_projection(self):
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        ab = WIDTH - (WIDTH // 4) + (RADIUS * cos_a)
        ac = HEIGHT // 2 + (RADIUS * sin_a)

        pygame.draw.line(self.game.screen, red,
                         circle_centre,
                         [WIDTH - (WIDTH // 4), ac], 4)

        pygame.draw.circle(self.game.screen, red,
                           (WIDTH - (WIDTH // 4), ac), 5)

        pygame.draw.line(self.game.screen, red,
                         [ab, ac],
                         [WIDTH - (WIDTH // 4), ac], 2)

        if len(self.values) > 0:
            pygame.draw.line(self.game.screen, red,
                             [WIDTH - (WIDTH // 4), ac],
                             [(WIDTH * SC_F) + abs(self.values[-1][0]) * 10, HEIGHT // 2 + self.values[-1][1] * RADIUS],
                             1)

    def draw_plot(self):
        for i in self.values:
            # cos
            pygame.draw.circle(self.game.screen, blue,
                               (WIDTH - WIDTH // 4 + i[2] * RADIUS, HEIGHT + i[0] * 10), 2)
            # sin
            pygame.draw.circle(self.game.screen, red,
                               ((WIDTH * SC_F) + abs(i[0]) * 10, HEIGHT // 2 + i[1] * RADIUS), 2)

    def draw(self):
        self.draw_x_projection()
        self.draw_y_projection()
        self.draw_hypotenuse()
        self.draw_plot()
