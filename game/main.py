import pygame
import random
from time import sleep
from settings import screen, clock, FPS, font
from cenas.game import Game
from cenas.game import reset_game
from cenas.menuu import draw_menu
from cenas.victory import draw_victory
from cenas.loser import draw_loser

pygame.init()
pygame.font.init()
running = True

state = "menu"

while running:
    dt = clock.tick(FPS) / 1000

    screen.fill((0, 0, 0))

    if state == "menu":
        new_state = draw_menu(screen, font)
        if new_state == "quit":
            running = False
        
        state = new_state

    elif state == "game":
        new_state = Game(dt)
        if new_state == "quit":
            running = False
        else:
            state = new_state

    elif state == "victory":
        new_state = draw_victory(screen, font)
        if new_state == "quit":
            running = False
        else:
            if new_state == "menu":
                reset_game()
        
        state = new_state

    elif state == "loser":
        new_state = draw_loser(screen, font)
        if new_state == 'quit':
            running = False
        else:
            if new_state == "menu":
                reset_game()

        state = new_state

    pygame.display.flip()

pygame.quit()