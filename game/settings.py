#configuraçôes do jogo
import pygame
import random
from entidades.enemy import Enemy
from sistema.timer import Timer
from entidades.vida import Vida

#configuraçoes da tela
screen = pygame.display.set_mode((800, 600))
FPS = 60
clock = pygame.time.Clock()
running = True
camsize = (2000, 2000)

#inimigos temporarios
def criarinimigos(qtd, world_rect, margin=100):
    inimigos = []
    for _ in range(qtd):
        x = random.randint(margin, world_rect.width - margin)
        y = random.randint(margin, world_rect.width - margin)
        inimigos.append(Enemy(x, y))
    
    return inimigos

# cria curas temporarias

def criarcuras(qtd, world_rect, margin=100):
    curas = []
    for _ in range(qtd):
        x = random.randint(margin, world_rect.width - margin)
        y = random.randint(margin, world_rect.width - margin)
        curas.append(Vida(x, y))
    
    return curas

#config dos temporizador
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 32)
tempo = (135) #140
gameover = False
victory = False

#configuraçoes da cura
curaval = 1

#configuraçoes do mapa
WORLD_WIDTH = 3100
WORLD_HEIGHT = 3100
world_rect = pygame.Rect(0, 0, WORLD_WIDTH, WORLD_HEIGHT)
