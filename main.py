import pygame
from alien import AlienType1, AlienType2, AlienType3
from loading_screen import LoadingScreen

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)  # Black
COUNTER_COLOR = (0, 255, 0)  # Bright green

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Demoscene Game")

# Create aliens
aliens = [
    AlienType1(),
    AlienType2(),
    AlienType3()
]

# Create loading screen
loading_screen = LoadingScreen(WINDOW_WIDTH, WINDOW_HEIGHT)

# Counter variables
collision_counter = 0

# Loading screen loop
loading = True
while loading:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    loading_screen.update()
    loading_screen.draw(window)
    pygame.display.flip()

    if loading_screen.finished_loading():
        loading = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    # Update and draw aliens
    for alien in aliens:
        alien.update()
        alien.draw(window)

    # Check collisions
    for i in range(len(aliens)):
        for j in range(i + 1, len(aliens)):
            if aliens[i].collides_with(aliens[j]):
                collision_counter += 1

    # Draw collision counter
    font = pygame.font.Font(None, 24)
    counter_text = font.render(f"Collisions: {collision_counter}", True, COUNTER_COLOR)
    window.blit(counter_text, (WINDOW_WIDTH - counter_text.get_width() - 10, WINDOW_HEIGHT - counter_text.get_height() - 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
