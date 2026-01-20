import pygame
from entidades.bala import Bullet

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.size = 20
        self.speed = 350

        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)

        self.bullets = []
        self.shoot_cooldown = 0.2
        self.shoot_timer = 0

        self.hp = 5
        self.invul_time = 0

        self.facing = pygame.Vector2(1, 0)  # direção atual

    def securar(self, hellar):
        if self.hp < 5:
            self.hp += hellar

    def take_damage(self, dmg=1):
        if self.invul_time <= 0:
            self.hp -= dmg
            self.invul_time = 1.0

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()
        move = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x += 1

        if move.length_squared() > 0:
            move = move.normalize()
            self.facing = move
            self.pos += move * self.speed * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return

        center = pygame.Vector2(self.rect.center)
        self.bullets.append(Bullet(center, self.facing))
        self.shoot_timer = self.shoot_cooldown

    def update(self, dt, screen_rect, camera, world_rect):
        self.shoot_timer -= dt

        self.handle_input(dt)

        self.pos.x = max(0, min(self.pos.x, world_rect.width - self.size))
        self.pos.y = max(0, min(self.pos.y, world_rect.height - self.size))
        self.rect.topleft = self.pos

        for b in self.bullets:
            b.update(dt, world_rect)

        self.bullets = [b for b in self.bullets if b.alive]

        if self.invul_time > 0:
            self.invul_time -= dt

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (255, 255, 255), camera.apply(self.rect))

        for b in self.bullets:
            pygame.draw.circle(
                screen,
                (255, 255, 255),
                camera.apply(pygame.Rect(b.pos.x, b.pos.y, 1, 1)).center,
                b.radius
            )
