import pygame
import random
from settings import screen, clock, FPS, camsize, victory, gameover, tempo, world_rect, WORLD_HEIGHT, WORLD_WIDTH, criarinimigos
from entidades.player import Player
from sistema.camera import Camera
from cenas.degubmap import draw_grid
from sistema.timer import Timer

pygame.init()
pygame.font.init()
running = True

Player = Player(200, 200)
timer = Timer(tempo)
font = pygame.font.SysFont(None, 32)
screen_rect = screen.get_rect()
camera = Camera(camsize)



def random_pos(margin=100):
    x = random.randint(margin, world_rect.width - margin)
    y = random.randint(margin, world_rect.height - margin)
    return x, y

#inimigos temporarios
inimigos = criarinimigos(10, world_rect)

#trem temporario
tx, ty = random_pos()
train_rect = pygame.Rect(tx, ty, 80, 50)

while pygame.Vector2(tx, ty).distance_to(Player.pos) < 400:
    tx, ty = random_pos()

train_rect.topleft = (tx, ty)

while running:
    dt = clock.tick(FPS)/1000

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    #atualizaçoes
    Player.update(dt, screen_rect, camera, world_rect)
    camera.follow(Player.rect, screen_rect)

    for e in inimigos:
        e.update(dt, pygame.Vector2(Player.rect.center))

    if not gameover and not victory:
        timer.update(dt)

        if timer.is_over():
            victory = True

    if Player.rect.colliderect(train_rect):
        victory = True

    #checa a colizão dos inimmigos com as balas
    for b in Player.bullets:
        for e in inimigos:
            if b.rect.colliderect(e.rect):
                b.alive = False
                e.tekedamge(1)
                e.aggro = True

    #checa a colizao dos inimigos com o Player
    for e in inimigos:
        e.update(dt, pygame.Vector2(Player.rect.center))

        if e.alive and Player.rect.colliderect(e.rect):
            Player.takedamage(1)


    Player.bullets = [b for b in Player.bullets if b.alive]
    inimigos = [e for e in inimigos if e.alive]


    #desenhos
    screen.fill((0, 0, 0))
    draw_grid(screen, camera, 32)

    #visualizaçao do mapa
    world_screen_rect = camera.apply(world_rect)
    pygame.draw.rect(screen, (255, 255, 255), world_screen_rect, 2)

    Player.draw(screen, camera)
    pygame.draw.rect(screen, (100, 200, 255), camera.apply(train_rect))

    for e in inimigos:
        e.draw(screen, camera, debug=True)

    #desenhos de textos
    timer.draw(screen, font)

    hp_text = font.render(f"Vida: {Player.hp}", True, (255, 255, 255))
    screen.blit(hp_text, (10, 40))


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()