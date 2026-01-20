import pygame

class Bullet:
    def __init__(self, pos, direction):
        self.pos = pygame.Vector2(pos)
        self.direction = direction.normalize()
        self.speed = 500
        self.radius = 4
        self.alive = True

        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.pos

    def update(self, dt, world_rect):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

        if not world_rect.collidepoint(self.pos):
            self.alive = False

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, self.radius)
