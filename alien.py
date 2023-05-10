import pygame
import numpy as np

class AlienType1:
    def __init__(self):
        self.ascii = ["  ___  ", " / _ \ ", "| (_) |", " \___/ "]
        self.color = (255, 0, 0)  # Red
        self.position = np.array([100, 100])
        self.velocity = np.array([1, 1])

    def update(self):
        self.position += self.velocity

    def draw(self, window):
        font = pygame.font.Font(None, 18)
        for i, line in enumerate(self.ascii):
            text_surface = font.render(line, True, self.color)
            window.blit(text_surface, self.position + np.array([0, i * font.get_linesize()]))

    def collides_with(self, other):
        rect_self = pygame.Rect(self.position[0], self.position[1],
                                len(self.ascii[0]) * 10, len(self.ascii) * 10)
        rect_other = pygame.Rect(other.position[0], other.position[1],
                                 len(other.ascii[0]) * 10, len(other.ascii) * 10)
        return rect_self.colliderect(rect_other)

class AlienType2:
    def __init__(self):
        self.ascii = ["  ____ ", " / ___|", "| |    ", "| |___ ", " \____|"]
        self.color = (0, 255, 0)  # Green
        self.position = np.array([200, 200])
        self.velocity = np.array([-1, 1])

    def update(self):
        self.position += self.velocity

    def draw(self, window):
        font = pygame.font.Font(None, 18)
        for i, line in enumerate(self.ascii):
            text_surface = font.render(line, True, self.color)
            window.blit(text_surface, self.position + np.array([0, i * font.get_linesize()]))

    def collides_with(self, other):
        rect_self = pygame.Rect(self.position[0], self.position[1],
                                len(self.ascii[0]) * 10, len(self.ascii) * 10)
        rect_other = pygame.Rect(other.position[0], other.position[1],
                                 len(other.ascii[0]) * 10, len(other.ascii) * 10)
        return rect_self.colliderect(rect_other)

class AlienType3:
    def __init__(self):
        self.ascii = ["   __  ", "  / _| ", " | |_  ", " |  _| ", " |_|   "]
        self.color = (0, 0, 255)  # Blue
        self.position = np.array([300, 300])
        self.velocity = np.array([1, -1])

    def update(self):
        self.position += self.velocity

    def draw(self, window):
        font = pygame.font.Font(None, 18)
        for i, line in enumerate(self.ascii):
            text_surface = font.render(line, True, self.color)
            window.blit(text_surface, self.position + np.array([0, i * font.get_linesize()]))

    def collides_with(self, other):
        rect_self = pygame.Rect(self.position[0], self.position[1],
                                len(self.ascii[0]) * 10, len(self.ascii) * 10)
        rect_other = pygame.Rect(other.position[0], other.position[1],
                                 len(other.ascii[0]) * 10, len(other.ascii) * 10)
        return rect_self.colliderect(rect_other)
