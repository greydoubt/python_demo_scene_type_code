import pygame
import numpy as np

class LoadingScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.loading_counter = 0
        self.loading_finished = False

    def update(self):
        # Simulate loading process
        self.loading_counter += 1
        if self.loading_counter >= 100:
            self.loading_finished = True

    def draw(self, window):
        # Transition background
        color_start = np.array([0, 255, 255])  # Cyan
        color_end = np.array([255, 0, 255])  # Magenta
        transition = self.loading_counter / 100.0
        background_color = tuple((color_start * (1 - transition) + color_end * transition).astype(int))

        window.fill(background_color)

        # "START THE DEMO" popup
        font = pygame.font.Font(None, 36)
        text_surface = font.render("START THE DEMO", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        window.blit(text_surface, text_rect)

        # "by greydoubt labs 2023"
        font = pygame.font.Font(None, 18)
        text_surface = font.render("by greydoubt labs 2023", True, (255, 255, 255))
        text_rect = text_surface.get_rect(midbottom=(self.width // 2, self.height - 50))
        window.blit(text_surface, text_rect)

    def finished_loading(self):
        return self.loading_finished
