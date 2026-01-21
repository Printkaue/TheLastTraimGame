import pygame
from sistema.camera import Camera

def draw_grid(screen, camera, cell_size=32, color=(40, 40, 40)):
    width, height = screen.get_size()

    # Descobre onde começa a grade no mundo
    start_x = int(camera.offset.x // cell_size) * cell_size
    start_y = int(camera.offset.y // cell_size) * cell_size

    for x in range(start_x, start_x + width + cell_size, cell_size):
        screen_x = x - camera.offset.x
        pygame.draw.line(screen, color, (screen_x, 0), (screen_x, height))

    for y in range(start_y, start_y + height + cell_size, cell_size):
        screen_y = y - camera.offset.y
        pygame.draw.line(screen, color, (0, screen_y), (width, screen_y))
