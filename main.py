# crashes on leaving edge

import pygame
import numpy as np

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Alien properties
aliens = [
    {
        "ascii": ["  ___  ", " / _ \ ", "| (_) |", " \___/ "],
        "color": (255, 0, 0),  # Red
        "position": np.array([100, 100]),
        "velocity": np.array([1, 1])
    },
    {
        "ascii": ["  ____ ", " / ___|", "| |    ", "| |___ ", " \____|"],
        "color": (0, 255, 0),  # Green
        "position": np.array([200, 200]),
        "velocity": np.array([-1, 1])
    },
    {
        "ascii": ["   __  ", "  / _| ", " | |_  ", " |  _| ", " |_|   "],
        "color": (0, 0, 255),  # Blue
        "position": np.array([300, 300]),
        "velocity": np.array([1, -1])
    }
]

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Demoscene Game")

# Create font object
font = pygame.font.Font(None, 18)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    for alien in aliens:
        # Update alien position
        alien["position"] += alien["velocity"]

        # Wrap alien around the screen
        if alien["position"][0] > WINDOW_WIDTH:
            alien["position"][0] = -font.size(alien["ascii"][0])[0]
        if alien["position"][1] > WINDOW_HEIGHT:
            alien["position"][1] = -font.size(alien["ascii"])[1]

        # Draw alien
        for i, line in enumerate(alien["ascii"]):
            text_surface = font.render(line, True, alien["color"])
            window.blit(text_surface, alien["position"] + np.array([0, i * font.get_linesize()]))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
