import pygame
import random
from settings import screen, clock, FPS, camsize, curaval, victory, gameover, tempo, world_rect, WORLD_HEIGHT, WORLD_WIDTH, criarinimigos, criarcuras
from entidades.player import Player
from sistema.camera import Camera
from core.degubmap import draw_grid
from sistema.timer import Timer

pygame.init()
pygame.font.init()

player = Player(200, 200)
timer = Timer(tempo)
font = pygame.font.SysFont(None, 32)
screen_rect = screen.get_rect()
camera = Camera(camsize)

def random_pos(margin=100):
    x = random.randint(margin, world_rect.width - margin)
    y = random.randint(margin, world_rect.height - margin)
    return x, y

#inimigos temporarios
inimigos = criarinimigos(25, world_rect)

#trem temporario
tx, ty = random_pos()
train_rect = pygame.Rect(tx, ty, 80, 50)

#curas temporarias
curas = criarcuras(10, world_rect)

while pygame.Vector2(tx, ty).distance_to(player.pos) < 1000:
    tx, ty = random_pos()

train_rect.topleft = (tx, ty)

def reset_game():
    global player, inimigos, curas, timer, victory, gameover, train_rect
    player = Player(200, 200)
    timer = Timer(tempo)
    font = pygame.font.SysFont(None, 32)
    screen_rect = screen.get_rect()
    camera = Camera(camsize)

    #inimigos temporarios
    inimigos = criarinimigos(25, world_rect)

    #trem temporario
    tx, ty = random_pos()
    train_rect = pygame.Rect(tx, ty, 80, 50)

    #curas temporarias
    curas = criarcuras(10, world_rect)

    while pygame.Vector2(tx, ty).distance_to(player.pos) < 400:
        tx, ty = random_pos()

    train_rect.topleft = (tx, ty)


def Game(dt):

    global inimigos, curas, victory, gameover, timer, player, screen_rect, running
        
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return "quit"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        player.shoot()


    #atualizaçoes
    player.update(dt, screen_rect, camera, world_rect)
    camera.follow(player.rect, screen_rect)

    #checa a colizao dos inimigos com o Player
    for e in inimigos:
        e.update(dt, pygame.Vector2(player.rect.center))

        if e.alive and player.rect.colliderect(e.rect):
            player.take_damage(1)
            if player.hp == 0:
                return "loser"

    if not gameover and not victory:
        timer.update(dt)

        if timer.is_over():
            victory = True
    else:
        if gameover or not victory:
            return "loser"
        
    if timer.time_left == 0:
        return "loser"

    if player.rect.colliderect(train_rect):
        victory = True
        return "victory"

    #checa a colizão dos inimmigos com as balas
    for b in player.bullets:
        for e in inimigos:
            if b.rect.colliderect(e.rect):
                b.alive = False
                e.tekedamge(1)
                e.aggro = True

    #checa a colisao do player coma cura
    for c in curas:
        if c.alive and player.rect.colliderect(c.rect):
            player.securar(curaval)
            c.alive = False

    player.bullets = [b for b in player.bullets if b.alive]
    inimigos = [e for e in inimigos if e.alive]
    curas = [c for c in curas if c.alive]


    #desenhos
    screen.fill((0, 0, 0))
    draw_grid(screen, camera, 32)

    #visualizaçao do mapa
    world_screen_rect = camera.apply(world_rect)
    pygame.draw.rect(screen, (255, 255, 255), world_screen_rect, 2)

    player.draw(screen, camera)
    pygame.draw.rect(screen, (100, 200, 255), camera.apply(train_rect))

    for e in inimigos:
        e.draw(screen, camera, debug=False)

    for c in curas:
        c.draw(screen, camera)

    #desenhos de textos
    timer.draw(screen, font)

    hp_text = font.render(f"Vida: {player.hp}", True, (255, 255, 255))
    screen.blit(hp_text, (10, 40))

    pygame.display.flip()
    return "game"