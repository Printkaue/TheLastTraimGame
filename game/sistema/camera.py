import pygame

class Camera:
    def __init__(self, size):
        self.offset = pygame.Vector2(0, 0)
        self.width, self.height = size

    def follow(self, target_rect, screen_rect):
        
        self.offset.x = target_rect.centerx - screen_rect.width // 2
        self.offset.y = target_rect.centery - screen_rect.height // 2

    def apply(self, rect):
        
        return rect.move(-self.offset.x, -self.offset.y)
