import pygame

pygame.init()
pygame.font.init()

def draw_victory(screen, font):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return "quit"

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                return "menu"

    txt = font.render("VOCE ESCAPOU", True, (50, 255, 50))
    info = font.render("Pressione ENTER para jogar novamente", True, (180, 180, 180))

    screen.blit(txt, txt.get_rect(center=(400, 220)))
    screen.blit(info, info.get_rect(center=(400, 270)))

    return "victory"
