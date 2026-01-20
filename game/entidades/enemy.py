import pygame

class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.size = 20
        self.speed = 120

        self.rect = pygame.Rect(x, y, self.size, self.size)

        self.aggro_radius = 100
        self.aggro = False
        self.alive = True

        self.life = 3

    def tekedamge(self, dmg=1):
        self.life -= dmg

        if self.life == 0:
            self.alive = False

    def update(self, dt, player_pos):
        # Distancia até o player
        to_player = player_pos - self.pos
        distance = to_player.length()

        # Ativa se entrar no raio
        if distance <= self.aggro_radius:
            self.aggro = True

        # Se estiver no aggro segue o jogador
        if self.aggro and distance > 0:
            direction = to_player.normalize()
            self.pos += direction * self.speed * dt
            self.rect.topleft = self.pos

    def draw(self, screen, camera, debug=False):
        pygame.draw.rect(screen, (200, 50, 50), camera.apply(self.rect))

        #debug
        if debug:
            center = camera.apply(self.rect).center
            pygame.draw.circle(screen, (80, 80, 80), center, self.aggro_radius, 1)

            