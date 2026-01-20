import pygame
from entidades.bala import Bullet
from sistema import camera

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

        self.faccing = pygame.Vector2(1, 0)

    def takedamage(self, dmg=1):
        if self.invul_time <= 0:
            self.hp -= dmg
            self.invul_time = 1.0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction.x += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()

        return direction

    def shoot(self, camera):
        mouse_screen = pygame.Vector2(pygame.mouse.get_pos())
        mouse_world = mouse_screen + camera.offset

        center = pygame.Vector2(self.rect.center)
        direction = mouse_world - center

        if direction.length_squared() == 0:
            return

        self.bullets.append(Bullet(center, direction))

    def update(self, dt, screen_rect, camera, world_rect):
        self.shoot_timer -= dt

        direction = self.handle_input()
        self.pos += direction * self.speed * dt
        self.rect.topleft = self.pos

        self.pos.x = max(0, min(self.pos.x, world_rect.width - self.size))
        self.pos.y = max(0, min(self.pos.y, world_rect.height - self.size))
        self.rect.topleft = self.pos


        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and self.shoot_timer <= 0:
            self.shoot(camera)
            self.shoot_timer = self.shoot_cooldown

        for b in self.bullets:

            b.update(dt, world_rect)
            self.bullets = [b for b in self.bullets if b.alive]

        if self.invul_time > 0:
            self.invul_time -= dt

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (255, 255, 255), camera.apply(self.rect))

        #Desenha as balas
        for b in self.bullets:
            pygame.draw.circle(
                screen,
                (255, 255, 255),
                camera.apply(pygame.Rect(b.pos.x, b.pos.y, 1, 1)).center,
                b.radius
            )
