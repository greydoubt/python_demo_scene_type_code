import pygame
import numpy as np

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
TEXT_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Demoscene Game")

# Create font object
font = pygame.font.Font(None, 36)

# Create text
text_surface = font.render("Hello, Demoscene!", True, TEXT_COLOR)

# Text position and velocity
text_pos = np.array([WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2])
text_velocity = np.array([1, 0])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    # Update text position
    text_pos += text_velocity

    # Wrap text around the screen
    if text_pos[0] > WINDOW_WIDTH:
        text_pos[0] = -text_surface.get_width()

    # Draw text
    window.blit(text_surface, text_pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
