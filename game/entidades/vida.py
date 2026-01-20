import pygame

class Vida:
    def __init__(self, x, y, size=12):

        self.pos = pygame.Vector2(x, y)
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)
        self.alive = True

    def draw(self, screen, camera):
        if not self.alive:
            return
        
        pygame.draw.rect(screen, (0, 255, 0), camera.apply(self.rect))

